# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A collection of reusable utilities for Claude Code: hooks, skills (custom slash commands), MCP server configs, and helper scripts. The `.claude/` directory is structured so that cloning this repo into a project makes skills and settings available directly.

## Repository Layout

- `.claude/skills/` — Custom slash commands, each a directory containing a `SKILL.md` with YAML frontmatter, invoked via `/skill-name`
- `.claude/settings.json` — Reference settings (contains machine-specific paths, adapt before use)
- `.claude/startup-quote.py` — Startup quote hook script
- `.claude/statusline.py` — Status line script
- `hooks/` — Claude Code hooks (pre/post tool-call scripts, triggered by `settings.json` hook config)
- `mcp/` — MCP server configurations and related scripts
- `scripts/` — General-purpose helper scripts

## How Utilities Are Used

The `.claude/` directory follows the standard Claude Code project layout. Skills in `.claude/skills/` are automatically available as slash commands when working in this repo. Scripts like `startup-quote.py` and `statusline.py` are referenced from `.claude/settings.json` and can be installed into `~/.claude/` for global use via the `/install` skill.

## Conventions

- **Skills** follow the Claude Code skills format: `.claude/skills/<name>/SKILL.md` with YAML frontmatter (`name`, `description`, `disable-model-invocation`, `allowed-tools`, `argument-hint`).
- Hooks and scripts should include a comment header documenting: what hook event they target, and the `settings.json` snippet needed to install them.
