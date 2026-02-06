# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A collection of reusable utilities for Claude Code: hooks, skills (custom slash commands), MCP server configs, and helper scripts. Users clone this repo and copy or symlink individual utilities into their own `~/.claude/` setup.

## Repository Layout

- `hooks/` — Claude Code hooks (pre/post tool-call scripts, triggered by `settings.json` hook config)
- `skills/` — Each skill is a directory containing a `SKILL.md` with YAML frontmatter, invoked via `/skill-name`
- `mcp/` — MCP server configurations and related scripts
- `scripts/` — General-purpose helper scripts
- Root-level scripts (`startup-quote.sh`, `startup-quote.py`) — Standalone utilities meant to be copied into `~/.claude/`

## How Utilities Are Used

Scripts in this repo are not run directly from this working directory. They are designed to be installed into a user's `~/.claude/` directory and referenced from `~/.claude/settings.json`. For example, the startup quote hook is configured in `settings.json` under `hooks.SessionStart` and invoked by Claude Code at session start.

## Conventions

- **Skills** follow the Claude Code skills format: `skills/<name>/SKILL.md` with YAML frontmatter (`name`, `description`, `disable-model-invocation`, `allowed-tools`, `argument-hint`).
- Hooks and scripts should include a comment header documenting: what hook event they target, and the `settings.json` snippet needed to install them.
- Both bash (`.sh`) and Python (`.py`) variants may exist for cross-platform support (see `startup-quote.sh` / `startup-quote.py`).
- The `settings.json` in the repo root is a reference example, not meant to be used as-is (it contains machine-specific paths).
