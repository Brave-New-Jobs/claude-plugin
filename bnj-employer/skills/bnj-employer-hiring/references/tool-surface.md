# BNJ employer tool surface

The 18 tools exposed by the Brave New Jobs employer connector, grouped by what
they are for. Every tool acts for the one company the connection is signed in to;
none takes a company as input. Read-only tools are safe to call freely.
`publish_job` with `confirmed: true` is the one irreversible step.

## Identity

| Tool | What it does | Changes anything? |
|---|---|---|
| `whoami` | The signed-in employer and the company this connection acts for. Call first. | No |
| `get_connector_info` | What the connector can and cannot do, and what stays in the dashboard. | No |

## Jobs

| Tool | What it does | Changes anything? |
|---|---|---|
| `list_jobs` | The company's jobs, newest first; filter by status or search text. | No |
| `get_job` | One job in full, with pipeline stages and screening questions. | No |
| `create_job` | A new job, always as a draft. Owner only. | Yes (draft, not public) |
| `update_job` | Change the fields passed. Live at once if the job is published. | Yes |
| `publish_job` | Without `confirmed`: returns the public content to show. With `confirmed: true`: publishes. | Yes, irreversible |

## Applications (read-only)

| Tool | What it does | Changes anything? |
|---|---|---|
| `list_applications` | Applications to the company's jobs, newest first; filter by job or status. | No |
| `get_application` | One application in full: answers and assessment. | No |
| `get_candidate_assessment` | Per-dimension and per-skill scores from the job's criteria. | No |

## Company profile (owner only)

| Tool | What it does | Changes anything? |
|---|---|---|
| `get_company_profile` | The public profile candidates see on every posting. | No |
| `update_company_profile` | Change the text fields passed; images untouched. | Yes, public |
| `set_company_image` | Replace the logo, cover image or favicon from a direct `https://` image link. | Yes, public |

## Odoo

| Tool | What it does | Changes anything? |
|---|---|---|
| `get_odoo_sync_status` | Whether Odoo is connected, last sync, what is not in Odoo yet. | No |
| `push_job_to_odoo` | Create one BNJ job in Odoo if missing. | Yes, in Odoo |
| `push_application_to_odoo` | Create one BNJ application in Odoo if missing; job must be there first. | Yes, in Odoo |
| `import_jobs_from_odoo` | Bring missing Odoo jobs into BNJ as drafts. Has a preview. | Yes (drafts) |
| `import_applications_from_odoo` | Bring missing Odoo applications and candidates into BNJ. Has a preview. | Yes |

There is no tool that moves an application through the pipeline, rejects a
candidate, leaves notes or feedback, manages colleagues, or touches billing. If
you are looking for one, it does not exist and its absence is deliberate: those
are done in the BNJ dashboard.
