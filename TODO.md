# TODO

- [x] Moved the evaluation harness from `claude_public_skills/eval` into `eval/`, renamed the
      skill directory to `digestif`, and documented it in the README evaluation section.
- [ ] Optional: direct API-key backends (Anthropic, OpenAI) as extra adapters, for users
      without an agent CLI installed.
- [ ] Optional: use agent session resume for repair rounds (`claude -c -p`,
      `codex exec resume --last`, `opencode run --continue`) instead of fresh invocations.
- [ ] Optional: `--chunk` for very long texts that exceed a single agent context.
- [ ] Raise the redundancy gate on long pieces or reduce repetition in Pass 3, the eval
      shows redundancy is the last metric under the pass gate.
