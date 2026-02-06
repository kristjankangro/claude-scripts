---
name: add-quote
description: Add a new parody quote to the startup quote collection
disable-model-invocation: true
argument-hint: [quote-text]
allowed-tools: Read, Edit
---

Add a new quote to both `startup-quote.py` and `startup-quote.sh` in this repo.

If `$ARGUMENTS` is provided, use it as the quote text. Otherwise ask the user what quote to add.

1. Read `startup-quote.py` and `startup-quote.sh` from the repo root.
2. Add the new quote to the `quotes` list/array in both files, matching the existing format:
   - Python: single-quoted string in the `quotes` list
   - Bash: double-quoted string in the `quotes` array
   - Escape inner quotes to match existing style in each file.
3. Tell the user the quote was added to both files.
