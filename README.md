# BraveNewJobs for Claude

Connect [BraveNewJobs](https://bravenewjobs.com) to Claude, so you can work with
your jobs, applications and candidates in conversation — including the two-way
Odoo Recruitment integration.

You need a BraveNewJobs account with Integrations enabled, and a Claude **Pro,
Max, Team or Enterprise** plan.

---

## If you use Claude Desktop, claude.ai or Cowork

Download **[`bnj-employer-plugin.zip`](../../releases/latest)** from the latest
release, then in Claude open **Customize → Plugins** and choose the option to
upload a custom plugin file. That is the connector and the skill in one go.

*In Cowork, open the **Cowork** tab first, then Customize.*

If you do not see a Plugins section — it is not on every plan and app version yet
— **[INSTALL.md](INSTALL.md)** has the two-step route that works everywhere: add
a connector, upload a skill. Same result, two minutes.

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
| `build-plugin-zip.py` | Builds `bnj-employer-plugin.zip` — the one-file install. |
| `build-skill-zip.py` | Builds the skill-only zip, for the two-step route. |

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

## A note on `.mcpb` files

If you have seen `.mcpb` bundles for other tools and wondered why this is not
one: that format ships a **local** MCP server — Node or Python that runs on your
own machine — and its manifest has no way to describe a remote server or to carry
a skill. The BraveNewJobs connector is remote and OAuth-protected, so there is
nothing to install locally. The plugin zip above is the single-file route here.

Do not put this server in `claude_desktop_config.json` either. That file is the
manual route for local servers; pointed at a remote OAuth server it does not
work, and it fails in a way that looks like a broken install.

## Building the zips yourself

```bash
python build-plugin-zip.py   # -> ./dist/bnj-employer-plugin.zip
python build-skill-zip.py    # -> ./dist/bnj-odoo-sync-skill.zip
```

They are shaped differently on purpose: the plugin zip has
`.claude-plugin/plugin.json` at its root, and the skill zip contains the skill
**folder** (`bnj-odoo-sync/SKILL.md`) rather than a bare `SKILL.md`. Each is what
its uploader expects.

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
