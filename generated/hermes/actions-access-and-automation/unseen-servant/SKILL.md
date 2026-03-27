---
name: unseen-servant
description: "Set up a persistent background automation that handles recurring maintenance tasks — dependency updates, stale branch cleanup, inbox triage, log rotation — silently and reliably. Use when routine work keeps piling up and you need a tireless helper that only surfaces when something requires your attention."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - literal
      - actions-access-and-automation
      - execution
      - automation
      - access
      - actuation
---
# Unseen Servant

Set up a persistent background automation that handles recurring maintenance tasks silently and reliably.

## When To Use

- Routine maintenance keeps piling up: dependency updates, stale branch cleanup, inbox triage, log rotation, cache purging.
- You want a helper that runs on a schedule or reacts to events, only surfacing when something needs your attention.
- The work is important but low-priority — it should happen reliably without competing for your focus.

## Procedure

1. **Define the mandate.** Specify exactly what the servant handles:
   - Which tasks (e.g., "close stale GitHub issues older than 90 days", "rotate logs over 100 MB").
   - Which surfaces (e.g., a specific repo, a Slack channel, a directory).
   - What is **off-limits** (e.g., "never delete branches with open PRs").

2. **Choose the cadence.** Pick one:
   - **Scheduled (cron)**: runs at fixed intervals (e.g., daily at 2 AM, weekly on Monday).
   - **Event-triggered**: runs in response to a webhook, file change, or CI event.
   - **Continuous**: polls a queue or watch target and acts when items appear.

3. **Set up the automation.** Examples:
   - **Stale branch cleanup**: `git branch --merged main | grep -v main | xargs git branch -d` in a weekly cron job.
   - **Dependency updates**: configure Dependabot or Renovate with auto-merge for patch versions.
   - **Log rotation**: add a logrotate config: `rotate 7, daily, compress, missingok`.
   - **Inbox triage**: create email filters or Slack workflow that labels/routes messages by keyword.

4. **Add logging.** Every action the servant takes must be recorded:
   - Write to a log file with timestamps: `echo "$(date -u +%FT%TZ) Deleted branch feature/old-experiment" >> servant.log`.
   - For GitHub Actions, the workflow run log serves as the audit trail.

5. **Add a kill switch.** Provide a way to stop the servant immediately:
   - A `PAUSE` file the servant checks before acting: `[[ -f .servant-pause ]] && exit 0`.
   - A toggle in CI (disable the workflow or cron job).
   - A Slack command that sets a flag.

6. **Review and adjust.** Check the activity log periodically. Tighten or expand the mandate based on what the servant handled vs. what it missed.

## Deliverables

- A running background automation (cron job, GitHub Action, or event-triggered script) with a documented mandate.
- An activity log with timestamps showing every action taken.
- A kill switch or pause mechanism the user can trigger immediately.

## Pitfalls / Guardrails

- The servant **never expands its own mandate** — it only touches what the user pre-approved.
- All actions must be logged and reviewable. Silent operation does not mean unaccountable operation.
- **Stop for confirmation** before any action that changes access, triggers an alert, or touches a production boundary.
- Provide a clear dismiss mechanism — the user must always be able to stop the servant immediately.

## Example

```
User: /unseen-servant I keep forgetting to clean up merged branches in our
      main repo. Set up something that handles this automatically.

Agent: Here is the plan for your branch cleanup servant:

       Mandate: delete local and remote branches that have been merged into
       main, excluding main, develop, and any branch with an open PR.

       Cadence: weekly, Monday at 6 AM UTC via GitHub Actions.

       Script:
         git fetch --prune origin
         for branch in $(git branch -r --merged origin/main | grep -v 'main\|develop'); do
           echo "$(date -u +%FT%TZ) Deleting $branch" >> cleanup.log
           git push origin --delete "${branch#origin/}"
         done

       Kill switch: add a file named .cleanup-pause to the repo root.
       The workflow checks for it before running.

       Shall I create the workflow file and test it on a dry run first?
```
