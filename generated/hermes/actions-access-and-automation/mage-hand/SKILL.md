---
name: mage-hand
description: "Make precise, minimal edits to files, records, configs, or structured data with the smallest possible blast radius. Use when you need a surgical change — renaming a field, patching a single config value, updating one record — without touching anything else."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - hybrid
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Mage Hand

Make precise, minimal edits to files, records, or system state with the smallest possible blast radius.

## When To Use

- You need a narrow, surgical edit: rename a field, patch a config value, update one database record, fix a typo in a doc.
- A broad refactor would be overkill — you want the smallest change that solves the problem.
- You want a clear before/after diff and an audit trail of exactly what was touched.

## Procedure

1. **Identify the target.** Name the exact file, record, config key, or field to change. State the success condition and any no-touch boundaries.

2. **Choose the smallest tool.** Prefer the most precise edit surface available:
   - Single file edit: `sed`, `jq`, or a targeted find-and-replace.
   - Config patch: edit the specific key, not the whole file.
   - Database record: `UPDATE ... WHERE id = X` (never `UPDATE` without a `WHERE`).
   - API call: `PATCH` a single field, not `PUT` the entire resource.

3. **Show the diff before applying.** Always preview the change:
   ```bash
   # Example: rename a JSON field in a config file
   jq '.oldFieldName as $v | del(.oldFieldName) | .newFieldName = $v' config.json > config.json.tmp
   diff config.json config.json.tmp
   ```

4. **Apply the change.** Execute the edit and confirm the result matches the preview.

5. **Report what was touched.** List:
   - What changed (with before/after values).
   - What was intentionally left alone (adjacent fields, related files).
   - Any side effects observed.

## Deliverables

- The completed edit with a before/after diff.
- An audit trail listing every file, record, or resource touched.
- A note on adjacent objects that were intentionally left alone.

## Pitfalls / Guardrails

- **Never apply broad changes** when a surgical edit is sufficient. If you are tempted to refactor, stop — that is a different skill.
- **Preserve user work** and unrelated state. If the file has uncommitted changes, warn before editing.
- **Always preview** before applying. A mage hand that moves the wrong object is worse than no hand at all.
- **One concern per invocation.** If multiple unrelated edits are needed, handle them as separate mage-hand operations.

## Example

```
User: /mage-hand The default timeout in our API config is 30s but it
      should be 60s. Just change that one value.

Agent: Target: src/config/api.yaml, field `server.timeout`
       No-touch: all other fields in api.yaml

       Before:
         server:
           timeout: 30

       After:
         server:
           timeout: 60

       Diff:
       -  timeout: 30
       +  timeout: 60

       Applied. No other fields were modified. Adjacent config files
       (database.yaml, cache.yaml) were not touched.
```
