# Brave New Jobs

Search the jobs that employers publish on [Brave New Jobs](https://www.bravenewjobs.com)
and apply to them in your conversation with Claude.

Search by role, skills, location, minimum salary, employment type and workplace
type, then read a job's full description, requirements, screening questions and
legal documents. To apply, choose a CV, answer the employer's screening
questions, add a cover letter and salary expectations if the employer asks for
them, and accept the employer's legal documents. You see a recap of everything
being sent and confirm it before anything reaches the employer. You can also
bookmark jobs and check the status of applications you have sent.

## What is in the plugin

|                              |                                                                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `.mcp.json`                  | The Brave New Jobs candidate connector, a remote MCP server at `https://mcp.bravenewjobs.com/mcp`. Nothing runs on your machine.               |
| `skills/bnj-apply-to-a-job/` | A skill that walks Claude through a complete, confirmed application: CV choice, screening answers, cover letter, legal consent and submission. |

The plugin has no hooks, commands, scripts or local servers.

## Install

**Claude Code:**

```bash
claude plugin marketplace add Brave-New-Jobs/claude-plugin
claude plugin install bnj-jobs@bravenewjobs
```

On claude.ai, Claude Desktop and Cowork, install it from the plugin directory.

The first time you use it, Claude asks you to sign in to Brave New Jobs. You
need a Brave New Jobs candidate account.

## What it sends, and where

- Everything goes to one place: Brave New Jobs, at `mcp.bravenewjobs.com`, over
  HTTPS. The plugin calls no other service and does not search the web.
- You sign in through a standard OAuth flow. Claude receives a token, never your
  password, and you can revoke it at any time.
- The connector reads and writes only your own records: your CVs, your draft and
  submitted applications, your screening answers and your saved jobs. It cannot
  see other candidates' data.
- An application goes only to the employer that posted the job, and only after
  you confirm it. Submitting is final.
- The conversation itself is not stored, quoted or summarised into your
  application.

Details: [Privacy notice](https://jobs.bravenewjobs.com/privacy) ·
[Terms of service](https://jobs.bravenewjobs.com/terms)

## Support

[jobs.bravenewjobs.com/support](https://jobs.bravenewjobs.com/support) ·
hello-bnj@bravenewjobs.com

## License

The files in this plugin are licensed under the [Apache License 2.0](LICENSE).
The Brave New Jobs service they connect to is governed by its
[terms of service](https://jobs.bravenewjobs.com/terms). The license grants no
rights to the Brave New Jobs name or logo.
