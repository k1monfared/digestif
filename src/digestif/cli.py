"""digestif command line."""

import argparse
import os
import shutil
import sys
from pathlib import Path

from . import __version__, agents
from . import pipeline

SKILL_DIR = pipeline.SKILL_DIR


def _agent_flags(p):
    p.add_argument("--agent", help="claude, codex or opencode (default: first detected)")
    p.add_argument("--agent-cmd", help="custom command template with {prompt}, {prompt_file}, {cwd}")
    p.add_argument("--model", help="model to pass through to the agent")


def _run_flags(p):
    p.add_argument("--retries", type=int, default=2,
                   help="repair rounds when validation fails (default: 2)")
    p.add_argument("--timeout", type=int, default=1800,
                   help="seconds allowed per agent invocation (default: 1800)")
    p.add_argument("--no-open", action="store_true", help="do not open the viewer in a browser")


def cmd_build(args):
    return pipeline.build(args)


def cmd_prep(args):
    return pipeline.prep(args)


def cmd_finish(args):
    return pipeline.finish(args)


def cmd_render(args):
    graph = Path(args.graph)
    if not graph.is_file():
        print("error: graph not found: %s" % args.graph)
        return 1
    run_dir = graph.parent
    code, out = pipeline.run_graph(run_dir, ["render", graph.name])
    if out:
        print(out)
    if code != 0:
        return code
    if not args.no_open:
        pipeline.open_viewer(run_dir)
    return 0


def cmd_validate(args):
    graph = Path(args.graph)
    if not graph.is_file():
        print("error: graph not found: %s" % args.graph)
        return 1
    code, out = pipeline.run_graph(graph.parent, ["validate", graph.name])
    print(out)
    return code


def cmd_open(args):
    target = Path(args.target)
    if target.is_dir():
        if not pipeline.open_viewer(target):
            print("error: no graph.html in %s" % target)
            return 1
        return 0
    if target.is_file() and target.suffix == ".html":
        import webbrowser
        webbrowser.open(target.resolve().as_uri())
        return 0
    print("error: %s is neither a run directory nor an html file" % target)
    return 1


def cmd_agents(args):
    found = agents.detected()
    print("digestif agent backends:\n")
    for name in agents.PREFERENCE:
        state, detail = agents.auth_status(name)
        mark = {"ok": "ready", "out": "installed, not ready", "missing": "not installed"}[state]
        print("  %-9s %s (%s)" % (name, mark, detail))
    print("\ncustom backends work too: --agent-cmd 'tool --prompt-file {prompt_file}'")
    if not found:
        print("\nno supported agent CLI found. Use 'digestif prep' for manual mode.")
    return 0


def cmd_doctor(args):
    problems = []
    print("python: %s" % sys.version.split()[0])
    if not SKILL_DIR.is_dir():
        problems.append("skill directory missing from the package: %s" % SKILL_DIR)
    else:
        print("skill: %s" % SKILL_DIR)
        code, out = pipeline.run_graph(SKILL_DIR, [
            "validate", str(SKILL_DIR / "examples" / "car-ban.graph.json")])
        if code == 0:
            print("renderer: ok")
        else:
            problems.append("renderer check failed:\n%s" % out)
    if shutil.which("node"):
        print("node: %s (headless UI tests available)" % shutil.which("node"))
    else:
        print("node: not found (headless UI tests unavailable, not required to use digestif)")
    for name in agents.PREFERENCE:
        state, detail = agents.auth_status(name)
        print("agent %-9s %s (%s)" % (name, state, detail))
    if not agents.detected():
        problems.append("no supported agent CLI found, use --agent-cmd or 'digestif prep'")
    if problems:
        print("\nproblems:")
        for p in problems:
            print("  - %s" % p)
        return 1
    print("\nall good")
    return 0


TARGETS = {
    "claude": lambda: Path.home() / ".claude" / "skills",
    "opencode": lambda: Path(os.environ.get("XDG_CONFIG_HOME", str(Path.home() / ".config")))
    / "opencode" / "skills",
    "project": lambda: Path.cwd() / ".claude" / "skills",
}


def cmd_install_skill(args):
    if args.dir:
        base = Path(args.dir)
    elif args.target:
        base = TARGETS[args.target]()
    else:
        print("error: pass --target {%s} or --dir DIR" % "|".join(TARGETS))
        return 1
    dest = base / "digestif"
    if dest.is_symlink() or dest.exists():
        if not args.force:
            print("error: %s already exists, pass --force to replace it" % dest)
            return 1
        if dest.is_symlink() or dest.is_file():
            dest.unlink()
        else:
            shutil.rmtree(dest)
    base.mkdir(parents=True, exist_ok=True)
    if args.link:
        dest.symlink_to(SKILL_DIR)
        print("linked %s -> %s" % (dest, SKILL_DIR))
    else:
        shutil.copytree(SKILL_DIR, dest)
        print("installed skill to %s" % dest)
    print("the skill is usable on its own, any agent that reads SKILL.md can follow it")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="digestif",
        description="Turn any text into a cited idea graph, a loglog outline and an "
                    "interactive viewer, using the agent CLI you already have.",
    )
    p.add_argument("--version", action="version", version="digestif %s" % __version__)
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("build", help="run the full pipeline and open the viewer")
    b.add_argument("input", help="path to a text file, or - for stdin")
    _agent_flags(b)
    _run_flags(b)
    b.add_argument("--out", default="digestif-runs", help="output root (default: ./digestif-runs)")
    b.add_argument("--slug", help="run folder name, default from the input file name")
    b.add_argument("--dry-run", action="store_true",
                   help="prepare the workspace and print the agent command, run nothing")
    b.set_defaults(func=cmd_build)

    pr = sub.add_parser("prep", help="prepare a workspace for any agent, no LLM call")
    pr.add_argument("input", help="path to a text file, or - for stdin")
    pr.add_argument("--out", default="digestif-runs", help="output root (default: ./digestif-runs)")
    pr.add_argument("--slug", help="run folder name, default from the input file name")
    pr.set_defaults(func=cmd_prep)

    f = sub.add_parser("finish", help="validate, repair, render and open an agent-written run")
    f.add_argument("run_dir", help="the run folder that contains graph.json")
    _agent_flags(f)
    _run_flags(f)
    f.set_defaults(func=cmd_finish)

    r = sub.add_parser("render", help="generate outline.log and graph.html, no agent")
    r.add_argument("graph", help="path to graph.json")
    r.add_argument("--no-open", action="store_true")
    r.set_defaults(func=cmd_render)

    v = sub.add_parser("validate", help="check graph integrity and citations")
    v.add_argument("graph", help="path to graph.json")
    v.set_defaults(func=cmd_validate)

    o = sub.add_parser("open", help="open a finished run in the browser")
    o.add_argument("target", help="run directory or an html file")
    o.set_defaults(func=cmd_open)

    a = sub.add_parser("agents", help="list detected agent CLIs and readiness")
    a.set_defaults(func=cmd_agents)

    d = sub.add_parser("doctor", help="environment check")
    d.set_defaults(func=cmd_doctor)

    i = sub.add_parser("install-skill", help="install or link the skill into an agent config")
    i.add_argument("--target", choices=sorted(TARGETS), help="claude, opencode or project")
    i.add_argument("--dir", help="custom directory to install into")
    i.add_argument("--link", action="store_true", help="symlink instead of copy")
    i.add_argument("--force", action="store_true", help="replace an existing install")
    i.set_defaults(func=cmd_install_skill)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
