#!/usr/bin/env python3
# Claude Code Status Line - Context Usage Monitor
#
# MANUAL SETUP REQUIRED:
# This script is NOT auto-executed. To enable it, add to your personal
# Claude Code settings (~/.claude/settings.json or via claude settings):
#
#   "statusLine": {
#     "type": "command",
#     "command": "python3 C:\\<project-location>\\.claude\\statusline.py"
#   }
#
# (Replace the path with your actual Palk directory)
# Review this script's contents before enabling.

import sys
import json
import subprocess

# Fix encoding on Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

try:
    data = json.load(sys.stdin)
except:
    print("Context: --")
    sys.exit(0)

# Extract data
model = data.get("model", {}).get("display_name", "Claude")
ctx = data.get("context_window", {})
percent = int(ctx.get("used_percentage", 0))
input_tokens = ctx.get("total_input_tokens", 0)
output_tokens = ctx.get("total_output_tokens", 0)

# Format token counts
def fmt(n):
    return f"{n // 1000}k" if n >= 1000 else str(n)

# Get git branch
def get_git_branch():
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            timeout=2
        )
        return result.stdout.strip() if result.returncode == 0 else None
    except:
        return None

# Get project directory name
def get_project_dir():
    try:
        import os
        # Get git root directory
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0:
            git_root = result.stdout.strip()
            return os.path.basename(git_root)
        # Fallback to current directory name
        return os.path.basename(os.getcwd())
    except:
        return None


# Color based on usage level
if percent < 50:
    color = "\033[32m"  # Green
elif percent < 70:
    color = "\033[33m"  # Yellow
elif percent < 85:
    color = "\033[38;5;208m"  # Orange
else:
    color = "\033[31m"  # Red
reset = "\033[0m"

# Build progress bar
bar_width = 10
filled = percent * bar_width // 100
bar = "█" * filled + "░" * (bar_width - filled)

# Get git info
branch = get_git_branch()
project = get_project_dir()

# Build status string parts
parts = []
parts.append(f"{color}{bar}{reset} {percent}%")
parts.append(f"in:{fmt(input_tokens)} out:{fmt(output_tokens)}")

if project:
    parts.append(project)

if branch:
    parts.append(branch)

parts.append(model)

# Output
print(" | ".join(parts))
