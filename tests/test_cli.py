"""CLI pipeline tests. No LLM calls: a fake agent installs canned graphs."""

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "src" / "digestif" / "skill" / "examples"
FIXTURES = ROOT / "tests" / "fixtures"
FAKE_AGENT = ROOT / "tests" / "fake_agent.py"


def run_cli(*args, cwd=None):
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src") + os.pathsep + env.get("PYTHONPATH", "")
    return subprocess.run(
        [sys.executable, "-m", "digestif.cli"] + [str(a) for a in args],
        capture_output=True, text=True, cwd=str(cwd or ROOT), env=env, timeout=300,
    )


def fake_agent_cmd(graph):
    return "%s %s --graph %s" % (sys.executable, FAKE_AGENT, graph)


def test_agents_lists_backends():
    r = run_cli("agents")
    assert r.returncode == 0, r.stderr
    assert "claude" in r.stdout and "codex" in r.stdout and "opencode" in r.stdout


def test_doctor_runs():
    r = run_cli("doctor")
    assert "python:" in r.stdout
    assert "renderer" in r.stdout


def test_prep_creates_workspace(tmp_path):
    r = run_cli("prep", EXAMPLES / "car-ban.txt", "--out", tmp_path)
    assert r.returncode == 0, r.stderr
    runs = list(tmp_path.iterdir())
    assert len(runs) == 1
    run_dir = runs[0]
    assert (run_dir / "source.txt").is_file()
    assert (run_dir / "AGENTS.md").is_file()
    assert (run_dir / "CLAUDE.md").read_text().strip() == "@AGENTS.md"
    assert (run_dir / "skill" / "SKILL.md").is_file()
    assert (run_dir / "skill" / "scripts" / "graph.py").is_file()
    assert not (run_dir / "graph.json").exists()
    assert "digestif finish" in r.stdout


def test_build_with_fake_agent(tmp_path):
    r = run_cli(
        "build", EXAMPLES / "car-ban.txt",
        "--out", tmp_path, "--agent-cmd", fake_agent_cmd(EXAMPLES / "car-ban.graph.json"),
        "--no-open",
    )
    assert r.returncode == 0, r.stdout + r.stderr
    run_dir = next(tmp_path.iterdir())
    for name in ["graph.json", "outline.log", "graph.html", "validation.txt", "run.log"]:
        assert (run_dir / name).is_file(), name
    graph = json.loads((run_dir / "graph.json").read_text())
    assert graph["meta"]["sourceText"]
    assert len(graph["meta"]["spans"]) == len(graph["meta"]["passages"])
    assert "Coverage: 5 of 5" in (run_dir / "outline.log").read_text()


def test_build_fails_cleanly_with_bad_graph(tmp_path):
    r = run_cli(
        "build", EXAMPLES / "car-ban.txt",
        "--out", tmp_path, "--agent-cmd", fake_agent_cmd(FIXTURES / "bad.graph.json"),
        "--retries", "1", "--no-open",
    )
    assert r.returncode == 1
    run_dir = next(tmp_path.iterdir())
    assert not (run_dir / "graph.html").exists()
    validation = (run_dir / "validation.txt").read_text()
    assert "error" in validation or "INVALID" in validation
    assert (run_dir / "repair.md").is_file()


def test_finish_on_prepared_run(tmp_path):
    r = run_cli("prep", EXAMPLES / "car-ban.txt", "--out", tmp_path)
    assert r.returncode == 0, r.stderr
    run_dir = next(tmp_path.iterdir())
    import shutil as _shutil
    _shutil.copyfile(EXAMPLES / "car-ban.graph.json", run_dir / "graph.json")
    r = run_cli("finish", run_dir, "--no-open")
    assert r.returncode == 0, r.stdout + r.stderr
    assert (run_dir / "graph.html").is_file()
    assert (run_dir / "outline.log").is_file()


def test_validate_and_render_examples(tmp_path):
    r = run_cli("validate", EXAMPLES / "car-ban.graph.json")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "coverage 5/5" in r.stdout
    r = run_cli("render", EXAMPLES / "car-ban.graph.json", "--no-open")
    assert r.returncode == 0, r.stdout + r.stderr


def test_install_skill_to_directory(tmp_path):
    r = run_cli("install-skill", "--dir", tmp_path)
    assert r.returncode == 0, r.stderr
    dest = tmp_path / "digestif"
    assert (dest / "SKILL.md").is_file()
    assert "name: digestif" in (dest / "SKILL.md").read_text()
    r = run_cli("install-skill", "--dir", tmp_path)
    assert r.returncode == 1
    r = run_cli("install-skill", "--dir", tmp_path, "--force")
    assert r.returncode == 0
