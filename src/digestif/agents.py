"""Agent CLI adapters.

Digestif does not call any model API directly. It drives the agent CLI the
user already has installed and logged in, in its headless mode, inside the
run workspace. Anything else can be plugged in with a command template.
"""

import json
import shlex
import shutil
import subprocess

PREFERENCE = ["claude", "codex", "opencode"]

LOGIN_HINT = {
    "claude": "claude auth login",
    "codex": "codex login",
    "opencode": "opencode auth login",
}


def _claude(prompt, cwd, model):
    argv = ["claude", "-p", prompt, "--allowedTools", "Read", "Write", "Edit", "Bash"]
    if model:
        argv += ["--model", model]
    return argv


def _codex(prompt, cwd, model):
    argv = ["codex", "exec", prompt, "--sandbox", "workspace-write", "--skip-git-repo-check"]
    if model:
        argv += ["--model", model]
    return argv


def _opencode(prompt, cwd, model):
    argv = ["opencode", "run", prompt, "--auto", "--dir", str(cwd)]
    if model:
        argv += ["--model", model]
    return argv


ADAPTERS = {
    "claude": {"bin": "claude", "build": _claude},
    "codex": {"bin": "codex", "build": _codex},
    "opencode": {"bin": "opencode", "build": _opencode},
}


def which(binary):
    return shutil.which(binary)


def detected():
    return [name for name in PREFERENCE if which(ADAPTERS[name]["bin"])]


def pick(name=None):
    if name:
        if name not in ADAPTERS:
            raise SystemExit(
                "unknown agent '%s', expected one of %s or --agent-cmd"
                % (name, ", ".join(PREFERENCE))
            )
        if not which(ADAPTERS[name]["bin"]):
            raise SystemExit(
                "'%s' is not installed. Install it or log in with: %s"
                % (ADAPTERS[name]["bin"], LOGIN_HINT.get(name, "see its docs"))
            )
        return name
    found = detected()
    if not found:
        raise SystemExit(
            "no agent CLI found (looked for %s).\n"
            "Install one, or run 'digestif prep <input>' and use any agent manually,\n"
            "or pass --agent-cmd with your own command template."
            % ", ".join(PREFERENCE)
        )
    return found[0]


def auth_status(name):
    """Best-effort login probe. Returns (state, detail) with state in ok/out/missing."""
    if name not in ADAPTERS:
        return ("out", "custom adapter")
    binary = ADAPTERS[name]["bin"]
    if not which(binary):
        return ("missing", "not installed, install it and run: %s" % LOGIN_HINT[name])
    try:
        if name == "claude":
            r = subprocess.run([binary, "auth", "status"], capture_output=True, text=True, timeout=30)
            try:
                data = json.loads(r.stdout.strip())
            except ValueError:
                return ("out", "cannot read auth status, run: %s" % LOGIN_HINT[name])
            if data.get("loggedIn"):
                return ("ok", data.get("authMethod") or "logged in")
            return ("out", "not logged in, run: %s" % LOGIN_HINT[name])
        if name == "opencode":
            r = subprocess.run([binary, "auth", "list"], capture_output=True, text=True, timeout=30)
            text = (r.stdout + r.stderr).strip()
            if "0 credentials" in text or not text:
                return ("out", "no providers configured, run: %s" % LOGIN_HINT[name])
            return ("ok", "providers configured")
        r = subprocess.run([binary, "--version"], capture_output=True, text=True, timeout=30)
        return ("out", "installed, log in with: %s" % LOGIN_HINT.get(name, "see its docs"))
    except Exception as exc:  # noqa: BLE001
        return ("out", "probe failed: %s" % exc)


def custom_argv(template, prompt, prompt_file, cwd):
    parts = shlex.split(template)
    if not parts:
        raise SystemExit("--agent-cmd is empty")
    mapping = {"{prompt}": prompt, "{prompt_file}": str(prompt_file), "{cwd}": str(cwd)}
    argv = []
    for part in parts:
        for token, value in mapping.items():
            part = part.replace(token, value)
        argv.append(part)
    return argv


def command(agent=None, agent_cmd=None, prompt="", prompt_file=None, cwd="", model=None):
    if agent_cmd:
        return custom_argv(agent_cmd, prompt, prompt_file or "", cwd)
    name = pick(agent)
    return ADAPTERS[name]["build"](prompt, cwd, model)
