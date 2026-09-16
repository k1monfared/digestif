"""The digestif pipeline: workspace, agent run, validation, repair, render."""

import re
import shlex
import shutil
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

from . import agents

SKILL_DIR = Path(__file__).resolve().parent / "skill"
GRAPH_PY = SKILL_DIR / "scripts" / "graph.py"

AGENTS_MD = """# Task: build graph.json from source.txt

You are running digestif, a text-to-idea-graph extraction. Read the full skill and follow it exactly:

- `skill/SKILL.md`

Input: `source.txt`, the complete source text.
Output: `graph.json`, the only file you may write.

Workflow:

1. Follow the skill's passes to build `graph.json` with full citations and full coverage.
2. Run `python3 skill/scripts/graph.py validate graph.json` and fix every error.
3. Run `python3 skill/scripts/graph.py locate graph.json source.txt -i` to add the source
   text and passage offsets. If a passage is reported as not found, your copied passage
   drifted from the source: fix the copy until locate succeeds. Never edit `source.txt`.
4. Do not create or edit `outline.log` or `graph.html`; the command line tool renders those
   afterwards. Do not write any other files.
"""

REPAIR_MD = """The graph.json in this directory is not accepted yet. Fix it in place, editing only
graph.json. Keep every node cited, keep coverage complete, and make locate succeed against
source.txt. The exact output of the last check follows.

"""


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")
    return slug[:48] or "text"


def read_input(arg):
    if arg == "-":
        return sys.stdin.read(), "stdin"
    path = Path(arg)
    if not path.is_file():
        raise SystemExit("input not found: %s" % arg)
    return path.read_text(encoding="utf-8"), path.stem


def create_workspace(out_root, slug, text, source_name):
    run_dir = Path(out_root) / ("%s-%s" % (slugify(slug), time.strftime("%Y%m%d-%H%M%S")))
    run_dir.mkdir(parents=True)
    (run_dir / "source.txt").write_text(text, encoding="utf-8")
    shutil.copytree(SKILL_DIR, run_dir / "skill")
    (run_dir / "AGENTS.md").write_text(AGENTS_MD, encoding="utf-8")
    (run_dir / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")
    return run_dir


def run_graph(run_dir, args):
    proc = subprocess.run(
        [sys.executable, str(GRAPH_PY)] + args,
        cwd=str(run_dir), capture_output=True, text=True,
    )
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def run_agent(argv, run_dir, log_path, timeout):
    header = "\n$ " + " ".join(shlex.quote(a) for a in argv) + "\n"
    with open(log_path, "a", encoding="utf-8") as log:
        log.write(header)
        log.flush()
        try:
            proc = subprocess.run(
                argv, cwd=str(run_dir), stdout=log, stderr=subprocess.STDOUT,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            log.write("\n[digestif] agent timed out after %s seconds\n" % timeout)
            return 124
    return proc.returncode


def invoke(run_dir, agent=None, agent_cmd=None, model=None, timeout=1800, prompt=None,
           prompt_file_name="prompt.md"):
    prompt = prompt or (
        "Work in this directory and do the task described in AGENTS.md. "
        "Read skill/SKILL.md first and follow it."
    )
    prompt_file = run_dir / prompt_file_name
    prompt_file.write_text(prompt, encoding="utf-8")
    argv = agents.command(
        agent=agent, agent_cmd=agent_cmd, prompt=prompt,
        prompt_file=prompt_file, cwd=run_dir, model=model,
    )
    return run_agent(argv, run_dir, run_dir / "run.log", timeout)


def validate_and_locate(run_dir, repair=None, retries=2, timeout=1800):
    """Validate, run locate, and repair through the agent when it fails.

    repair is a callable(prompt) -> None that invokes the agent, or None to
    validate only.
    """
    last = ""
    for attempt in range(retries + 1):
        code, out = run_graph(run_dir, ["validate", "graph.json"])
        if code == 0:
            code2, out2 = run_graph(run_dir, ["locate", "graph.json", "source.txt", "-i"])
            if code2 == 0:
                return True, out + "\n" + out2
            out = out2
        last = out
        if repair is None or attempt >= retries:
            break
        (run_dir / "repair.md").write_text(
            REPAIR_MD + "```\n" + out + "\n```\n", encoding="utf-8"
        )
        repair(
            "The graph.json you produced was rejected. Follow repair.md in this directory, "
            "fix graph.json only, and rerun validate and locate until they both succeed."
        )
    return False, last


def render(run_dir):
    return run_graph(run_dir, ["render", "graph.json"])


def open_viewer(run_dir):
    html = Path(run_dir) / "graph.html"
    if html.is_file():
        webbrowser.open(html.resolve().as_uri())
        return True
    return False


def announce(step, total, message):
    print("[%d/%d] %s" % (step, total, message), flush=True)


def build(args):
    text, source_name = read_input(args.input)
    run_dir = create_workspace(args.out, args.slug or source_name, text, source_name)
    total = 4
    announce(1, total, "workspace ready: %s" % run_dir)

    if args.dry_run:
        argv = agents.command(
            agent=args.agent, agent_cmd=args.agent_cmd, prompt="(dry run)",
            prompt_file=run_dir / "prompt.md", cwd=run_dir, model=args.model,
        )
        print("agent command would be:\n  " + " ".join(shlex.quote(a) for a in argv))
        print("workspace kept at %s" % run_dir)
        return 0

    def repair(prompt):
        announce(1, total, "repair round: asking the agent to fix graph.json")
        return invoke(run_dir, args.agent, args.agent_cmd, args.model, args.timeout,
                      prompt=prompt, prompt_file_name="repair_prompt.md")

    invoke(run_dir, args.agent, args.agent_cmd, args.model, args.timeout)
    announce(2, total, "agent finished, validating")
    graph = run_dir / "graph.json"
    if not graph.is_file():
        print("error: the agent did not produce graph.json, see %s" % (run_dir / "run.log"))
        return 1

    ok, out = validate_and_locate(run_dir, repair=repair, retries=args.retries,
                                  timeout=args.timeout)
    (run_dir / "validation.txt").write_text(out + "\n", encoding="utf-8")
    if not ok:
        print("error: graph.json did not validate after %d attempt(s)" % (args.retries + 1))
        print(out)
        print("workspace kept at %s" % run_dir)
        return 1
    announce(3, total, "graph valid, citations located, rendering")
    code, out = render(run_dir)
    if code != 0:
        print("error: rendering failed\n%s" % out)
        return 1
    announce(4, total, "wrote %s" % (run_dir / "outline.log"))
    announce(4, total, "wrote %s" % (run_dir / "graph.html"))
    if not args.no_open:
        open_viewer(run_dir)
    print("done: %s" % run_dir)
    return 0


def prep(args):
    text, source_name = read_input(args.input)
    run_dir = create_workspace(args.out, args.slug or source_name, text, source_name)
    print("workspace ready: %s\n" % run_dir)
    print("Open your agent (Claude Code, Codex, opencode, a chat window) in that folder and say:\n")
    print('  "Do the task in AGENTS.md. Read skill/SKILL.md first and follow it."\n')
    print("When graph.json exists, finish the run with:")
    print("  digestif finish %s" % run_dir)
    return 0


def finish(args):
    run_dir = Path(args.run_dir)
    if not (run_dir / "graph.json").is_file():
        print("error: no graph.json in %s" % run_dir)
        return 1
    def repair(prompt):
        announce(1, 3, "repair round: asking the agent to fix graph.json")
        return invoke(run_dir, args.agent, args.agent_cmd, args.model, args.timeout,
                      prompt=prompt, prompt_file_name="repair_prompt.md")

    repair_fn = repair if (args.agent or args.agent_cmd or agents.detected()) else None
    ok, out = validate_and_locate(run_dir, repair=repair_fn, retries=args.retries,
                                  timeout=args.timeout)
    (run_dir / "validation.txt").write_text(out + "\n", encoding="utf-8")
    if not ok:
        print("error: graph.json did not validate")
        print(out)
        return 1
    announce(2, 3, "valid and cited, rendering")
    code, out = render(run_dir)
    if code != 0:
        print("error: rendering failed\n%s" % out)
        return 1
    announce(3, 3, "wrote %s" % (run_dir / "outline.log"))
    announce(3, 3, "wrote %s" % (run_dir / "graph.html"))
    if not args.no_open:
        open_viewer(run_dir)
    print("done: %s" % run_dir)
    return 0
