# CODEX.md

## Local Skills

This project mirrors generated spell skills from `generated/openclaw/` into `.codex/skills/` for local Codex use.

- Install or refresh them with `CODEX_HOME=$PWD/.codex npm run install:codex-skills`.
- When a user invokes `$skill-name` and `.codex/skills/<skill-name>/SKILL.md` exists, load that file and follow it as a project-local skill.
- Do not hand-edit generated skills in `generated/`; regenerate them from the source data and renderer.
