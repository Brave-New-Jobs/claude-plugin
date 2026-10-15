# Brave New Jobs for Claude

Plugins that connect [Brave New Jobs](https://www.bravenewjobs.com) to Claude.

| Plugin | For | What it does |
|---|---|---|
| [`bnj-jobs`](bnj-jobs/) | Candidates | Search the jobs published on Brave New Jobs and apply to them in the conversation. |
| [`bnj-employer`](bnj-employer/) | Employers | Draft and publish jobs, review applications, keep your company profile current and sync with Odoo. |

Each plugin is a remote Brave New Jobs connector plus the skills Claude uses to
work with it. Nothing runs on your machine. Each plugin's README says exactly
what it connects to and what data it handles.

## Install

On claude.ai, Claude Desktop and Cowork, install from the plugin directory.

In Claude Code:

```bash
claude plugin marketplace add Brave-New-Jobs/claude-plugin
claude plugin install bnj-jobs@bravenewjobs        # candidates
claude plugin install bnj-employer@bravenewjobs    # employers
```

Claude asks you to sign in to Brave New Jobs the first time you use either one.

Already installed `bnj-employer` from here before? Run
`claude plugin marketplace update bravenewjobs` and then
`claude plugin update bnj-employer@bravenewjobs`.

## Support

hello-bnj@bravenewjobs.com ·
[Privacy notice](https://jobs.bravenewjobs.com/privacy) ·
[Terms of service](https://jobs.bravenewjobs.com/terms)

## License

[Apache License 2.0](bnj-jobs/LICENSE), per plugin folder. The license covers
the files in this repository, not the Brave New Jobs service or its name and
logo.
