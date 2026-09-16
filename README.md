# BraveNewJobs for Claude

Connect [BraveNewJobs](https://bravenewjobs.com) to Claude, so you can work with
your jobs, applications and candidates in conversation — including the two-way
Odoo Recruitment integration.

You need a BraveNewJobs account with Integrations enabled, and a Claude **Pro,
Max, Team or Enterprise** plan.

---

## If you use Claude Desktop or claude.ai

**Read [INSTALL.md](INSTALL.md).** It is written for a non-technical reader and
takes about two minutes: add a connector, upload a skill. You do not need this
repository or anything else on this page.

## If you use Claude Code

Install both halves as one plugin:

```bash
claude plugin marketplace add Brave-New-Jobs/claude-plugin
claude plugin install bnj-employer@bravenewjobs
```

Then start a session and ask *"Is our Odoo connected, and what is waiting to
sync?"*. You will be asked to sign in to BraveNewJobs the first time.

---

## What is in here

| | |
|---|---|
| `.mcp.json` | The BraveNewJobs employer connector — a remote, OAuth-protected MCP server. Nothing runs on your machine. |
| `skills/bnj-odoo-sync/` | A skill that teaches Claude how the Odoo integration actually behaves, so you get straight answers rather than guesses. |
| `INSTALL.md` | The two-step setup for Claude Desktop and claude.ai. |
| `build-skill-zip.py` | Packages the skill as a zip for upload to Claude Desktop. |

## What the Odoo sync does

Jobs and applications travel in both directions between Odoo Recruitment and
BraveNewJobs, on demand — never on a schedule, and never without you asking.

**The one rule worth knowing before you start: the sync only ever creates what is
missing. It never changes a record that already exists on the other side.** Edit
a job in Odoo after it has synced and BraveNewJobs keeps what it already had, and
the same in reverse. That is deliberate — it is what stops two systems silently
overwriting each other's work — but it is also the thing most people assume
wrongly, so it is worth saying plainly.

Because of that, running a sync twice is safe and quiet: everything is already
paired, so nothing is created.

An import never publishes a job, never emails a candidate, never runs AI scoring
on imported applications, never creates a login for an imported candidate, and
never deletes anything on either side.

## Why there is no one-click installer

`.mcpb` (MCP Bundle) is the single-file, one-click install format for Claude
Desktop, and it cannot carry this. Its manifest allows four server types —
`node`, `python`, `binary`, `uv` — all of them local processes launched with a
command, and it has no field for a skill. The BraveNewJobs connector is a
**remote** OAuth server, so there is nothing to bundle and run locally.

Remote servers are added as **custom connectors**, which is already a single URL
paste, and skills are uploaded separately. That is what `INSTALL.md` walks
through.

Do not put this server in `claude_desktop_config.json`. That file is the manual
route for local servers; pointed at a remote OAuth server it does not work, and
it fails in a way that looks like a broken install.

## Building the skill zip yourself

```bash
python build-skill-zip.py            # -> ./dist/bnj-odoo-sync-skill.zip
python build-skill-zip.py ~/Desktop  # -> somewhere else
```

The zip contains the skill **folder** (`bnj-odoo-sync/SKILL.md`), which is what
Claude expects — not a bare `SKILL.md`.

---

## Security

This repository contains no credentials, and it never will. Authentication is
OAuth: you sign in to BraveNewJobs yourself, Claude receives a scoped token it
can use on your behalf, and you can revoke it at any time from the Connectors
screen. Nothing here holds an API key, and you should never be asked to paste one
into a config file to use this plugin.

The connector is scoped to the single company your BraveNewJobs account belongs
to. It cannot see another customer's data, and no other customer can see yours.

## Support

**support@bravenewjobs.com**

Copyright © BraveNewJobs. All rights reserved.
