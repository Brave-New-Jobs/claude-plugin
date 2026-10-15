# Brave New Jobs for Employers

Run your company's hiring on [Brave New Jobs](https://www.bravenewjobs.com) from
your conversation with Claude.

Draft, edit and publish jobs, see who applied and how candidates scored, keep
your company's public profile and logo current, and move jobs and applications
between Brave New Jobs and your Odoo Recruitment. Claude acts for the one
company your account belongs to, within your role on the team: owners,
managers and HR can make changes; interviewers and auditors can only read.
Publishing always waits for your explicit confirmation.

## What is in the plugin

|                               |                                                                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.mcp.json`                   | The Brave New Jobs employer connector, a remote MCP server at `https://employer-mcp.bravenewjobs.com/mcp`. Nothing runs on your machine.             |
| `skills/bnj-employer-hiring/` | How to draft and publish jobs, review applications, keep the company profile current, and what still has to be done in the Brave New Jobs dashboard. |
| `skills/bnj-odoo-sync/`       | How the Odoo integration behaves: what an import or push creates, what it leaves behind, and how to read a sync report.                              |
| `INSTALL.md`                  | Step-by-step setup for claude.ai and Claude Desktop, including a route without plugin upload.                                                        |

The plugin has no hooks, commands, scripts or local servers.

## Install

**Claude Code:**

```bash
claude plugin marketplace add Brave-New-Jobs/claude-plugin
claude plugin install bnj-employer@bravenewjobs
```

On claude.ai, Claude Desktop and Cowork, install it from the plugin directory,
or follow [INSTALL.md](INSTALL.md).

The first time you use it, Claude asks you to sign in with your Brave New Jobs
employer account.

## What it sends, and where

- Everything goes to one place: Brave New Jobs, at `employer-mcp.bravenewjobs.com`,
  over HTTPS. The plugin calls no other service.
- You sign in through a standard OAuth flow. Claude receives a token, never your
  password, and you can revoke it at any time.
- The connector reads and writes only your own company's jobs, applications,
  candidates and profile, within the permissions of your role.
- The Odoo sync runs on Brave New Jobs' servers, which talk to your Odoo
  directly. No Odoo credential, CV file or applicant record passes through the
  conversation. A sync only creates what is missing on the other side; it never
  changes or deletes an existing record, never publishes a job and never emails
  anyone.

Details: [Privacy notice](https://jobs.bravenewjobs.com/privacy) ·
[Terms of service](https://jobs.bravenewjobs.com/terms)

## Support

hello-bnj@bravenewjobs.com

## License

The files in this plugin are licensed under the [Apache License 2.0](LICENSE).
The Brave New Jobs service they connect to is governed by its
[terms of service](https://jobs.bravenewjobs.com/terms). The license grants no
rights to the Brave New Jobs name or logo.
