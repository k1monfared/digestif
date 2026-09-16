# TODO

- [ ] Move the evaluation harness from `claude_public_skills/eval` into this repo: the frozen
      corpus, judge prompts, runner, and the run history directories. Also rename its skill
      directory from `point-hierarchy` to `digestif` and update the config references.
      Waiting because an evaluation run was still active when this repo was created
      (2026-09-15). Do it once that run finishes. Remove the matching note from README.md
      and AGENTS.md when done.
- [ ] Optional: direct API-key backends (Anthropic, OpenAI) as extra adapters, for users
      without an agent CLI installed.
- [ ] Optional: use agent session resume for repair rounds (`claude -c -p`,
      `codex exec resume --last`, `opencode run --continue`) instead of fresh invocations.
- [ ] Optional: `--chunk` for very long texts that exceed a single agent context.
