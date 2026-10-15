# BNJ tool surface

The 26 tools exposed by the Brave New Jobs MCP server for Claude, grouped by
what they are for. Read-only tools are safe to call freely. `submit_application`
is the one irreversible step. Every tool requires the candidate to be signed in
to BNJ through the connector.

There is no tool that stores, quotes or summarises the conversation, and no tool
that rates, scores or profiles the candidate. If you are looking for one, it does
not exist and its absence is deliberate.

## Finding work

| Tool | Read-only | What it does |
|---|---|---|
| `search_jobs` | yes | Filtered search over published jobs: keywords, location, minimum salary, employment type, workplace type, department. |
| `get_job_details` | yes | Full profile for one job: description, `fieldRequirements`, screening questions, employer info, legal documents. |
| `save_job` | no | Bookmarks a job. |
| `saved_jobs` | yes | Lists bookmarked jobs. |

## Session

| Tool | Read-only | What it does |
|---|---|---|
| `check_login_status` | yes | Reports who is signed in. |
| `logout` | no | Clears the session and any open draft. Stored data is untouched. |

## CVs

| Tool | Read-only | What it does |
|---|---|---|
| `list_my_cvs` | yes | Lists the candidate's uploaded CVs (up to 5), and whether each has structured data. |
| `get_cv_upload_link` | yes | Returns the browser page where the candidate uploads a CV. Starts no upload itself. |
| `select_cv_for_application` | no | Pins an existing CV to the application. Checks ownership and upload confirmation. |
| `get_cv_text` | yes | Plain text of a stored CV. |
| `get_cv_json_schema` | yes | The CV shape BNJ expects. |
| `upload_cv_data` | no | Attaches the structured CV to an uploaded CV file (`cv_file_id`), or on its own on jobs that accept the CV without the file. |

Accepted uploads: pdf, doc, docx. Max 5 MB, max 5 files per kind per candidate.

## Cover letters

| Tool | Read-only | What it does |
|---|---|---|
| `list_my_cover_letters` | yes | Lists the candidate's uploaded cover letters (up to 5). |
| `get_cover_letter_upload_link` | yes | Returns the browser page where the candidate uploads a cover letter. |
| `select_cover_letter_for_application` | no | Pins an uploaded cover letter to the application. |
| `set_cover_letter_text` | no | Attaches an inline cover letter, before or after the draft is opened. Replaces earlier text. |

## Building the application

| Tool | Read-only | What it does |
|---|---|---|
| `start_application` | no | Opens a draft. Takes an optional inline `cover_letter`. Refuses if the candidate already applied to this job, unless that application was withdrawn, rejected or disqualified. |
| `answer_screening` | no | Records the answer to the current screening question and returns the next one. |
| `prefill_answers` | no | Records several answers at once, drawn from the CV. Get the candidate's agreement first. |
| `process_cv` | no | Renders the CV alongside the still-unanswered questions. Records nothing. |
| `set_inference_preference` | no | Sets whether the CV may be used to suggest screening answers. |
| `set_expected_salary` | no | Sets the expected salary (defaults: EUR, per year). |
| `update_application` | no | Sets any of `expected_salary`, `notice_period_days` (0 = immediately, 91 = more than 3 months), `cover_letter_text`, `allow_inference` in one call. Use it for any field it covers. |
| `acknowledge_legal_documents` | no | Records which mandatory documents the candidate accepted. A second call replaces the first. |
| `submit_application` | no, irreversible | Files the application. Requires `confirmed: true`. |
| `my_applications` | yes | Lists the candidate's own applications and their status. |

## Notes

- Nothing reaches the employer before `submit_application`. Draft state lives in
  the session until then, and `logout` discards an open draft; nothing touches a
  submitted application.
- All ids are UUIDs returned by a previous tool. Never construct one.
- No tool reaches outside BNJ's own database, file storage and sign-in service.
- The application is built from the candidate's CV, their screening answers and
  their cover letter. Nothing else about them is collected through this channel.
