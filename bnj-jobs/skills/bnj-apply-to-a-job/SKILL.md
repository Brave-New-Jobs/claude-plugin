---
name: bnj-apply-to-a-job
description: Apply to a Brave New Jobs role end-to-end inside the conversation, with no application forms. Use when the user wants to find work, asks anything about a BNJ job or employer (pay, benefits, remote work, the company, the team), shares a CV to be matched against openings, or asks to apply, prepare, review or submit an application. Covers CV selection, cover letters, screening answers, legal consent and the confirmed submission.
---

# Applying to a job on Brave New Jobs

Brave New Jobs (BNJ) is an agent-native hiring channel. Candidates apply through
conversation: no application forms, no CAPTCHAs. The application itself is assembled from
what the candidate provides — their CV, their answers to the employer's screening
questions, and their cover letter. BNJ evaluates the match on its own servers.
Employers value these applications precisely because they are not keyword-padded
form submissions.

The conversation is how the application gets built. It is not itself stored,
quoted or summarised into the application, and you have no tool for doing so.

Everything below runs on the `bnj-jobs` MCP server bundled with this plugin.
Tool names are listed in `references/tool-surface.md`.

## How to talk to the candidate

The candidate is a job seeker, not an engineer. Use plain, everyday language.

Never narrate internal mechanics. Avoid "structured data", "parsing", "upload",
"object", "endpoint", "schema", "tool call". Instead of "the selected CV already
has structured data attached, so no parsing/upload is needed", say "I can use the
CV already on your profile, nothing else needed there".

## Guiding the candidate

Lead the candidate through the application. Do not leave them to work out what
comes next.

- **Show the way.** Once they want to apply, tell them briefly what this job's
  application involves (for example: choose a CV, answer the employer's screening
  questions, accept the employer's legal documents, check a final recap). As you
  go, say which step you are on and what comes next. Ask one thing at a time.
- **Overview first, whatever comes up.** Your first reply after the candidate
  says they want to apply carries the overview, the "now gathering information"
  statement and the "nothing is sent until you confirm" statement below. Give
  them even when a tool result raises something to sort out (a CV in another
  name, a missing upload, an earlier application): raise that after the
  overview, in the same reply, never instead of it.
- **Say clearly when collection starts.** Searching and reading about jobs
  gathers nothing for an application. Before the first step that does (choosing
  or sharing a CV for this job, opening the draft with `start_application`, or
  answering a screening question), tell the candidate in plain words that from
  now on you are gathering information for their application to this job at this
  employer. Never start gathering it silently.
- **Nothing is sent until they say so.** At that same moment, tell them that
  everything they give you is kept as a draft only: nothing is sent to the
  employer, and no application is submitted, until they have seen the final
  recap and told you they want to send it. Keep that promise. `submit_application`
  is the only step that sends anything, and you call it only after that explicit
  confirmation (see "Submitting").
- **They can ask anything.** Tell them they are free to ask anything about the
  job or the employer, before or at any point during the application. When they
  ask, pause the application, answer from `get_job_details` (the description,
  requirements, employer information and legal documents), then pick up where
  you left off. If BNJ does not have the answer, say so plainly and suggest they
  ask the employer. Never invent facts about the job or the employer, and do not
  fill the gap with outside knowledge either, even when it is true in general
  (typical benefits, legal minimums, market rates): the candidate would read it as
  what this employer offers. A question is not an answer: never record something
  the candidate asked as part of their application.
- **Point out the company profile.** When `get_job_details` includes an
  "About" section describing the employer (its tagline and description), tell
  the candidate, when you present the job, that they can ask you about the
  company as well as the role. Say it in one short line, once per job, and
  answer only from that section and the rest of the job details.

## The sequence

1. **Find the role.** `search_jobs` for keywords, location, salary, employment
   type, workplace type or department.
2. **Read it properly.** `get_job_details` before applying. It returns the
   description, the application requirements (`fieldRequirements`), the screening
   questions, employer information and any legal documents.
3. **Say that the application is starting** (see "Guiding the candidate"):
   what the steps are, that you are now gathering information for this
   application, that nothing is sent until they confirm, and that they can ask
   about the job or the employer at any time.
4. **Settle the CV** (see "CV rules").
5. **Settle the cover letter** (see "Cover letter rules"), then
   `start_application({ job_id })` to open a draft. Nothing is sent to the
   employer at this point.
6. **Answer the screening questions.** They come one at a time: answer the
   current one with `answer_screening`, and the response shows the next. Or record
   several at once with `prefill_answers`, which records the answers on the draft,
   so show the candidate what you are about to record and get their agreement
   first. `process_cv` shows the CV alongside the still-unanswered questions when
   working out what the CV supports.
7. **Fill the remaining fields.** `update_application` sets the expected salary
   and the notice period when the job asks for them, in one call if you have
   both. Ask the candidate for the figure and how soon they could start; never
   guess either.
8. **Accept the legal documents** with `acknowledge_legal_documents` if the job
   has any. Show the candidate each document's link first and wait for their
   explicit agreement. Never accept on their behalf.
9. **Recap, confirm, submit.** See "Submitting" below.

`set_inference_preference` sets whether the CV may be used to suggest screening
answers. `save_job` bookmarks a role for later; `saved_jobs` lists them.
`my_applications` answers "have I already applied?" and "where did I apply?".

## CV rules

When the candidate shares a CV, tell them plainly, in everyday words, that the
information in it is read and used to check how well they match the job. Brave
New Jobs does that check, not the employer: never say the employer reads the CV
before the candidate has confirmed and the application is sent.

Jobs differ in what they need, and `get_job_details` says which applies through
`fieldRequirements.cv_original_file`:

- **The job requires the original CV file** (absent or `"required"`). Tell the
  candidate the application also needs the file itself, uploaded on the BNJ
  upload page. An already-uploaded CV can be reused. The application cannot be
  submitted without it.
  1. `list_my_cvs` to see what is on their profile.
  2. If the list is empty, `get_cv_upload_link`, show them the link, and wait
     until they say the upload is done. Then `list_my_cvs` again.
  3. Ask which CV to use, then `select_cv_for_application({ cv_file_id })`.
  4. If that CV has no structured data yet, read it with `get_cv_text`, turn it
     into the shape `get_cv_json_schema` returns without changing that shape, and
     attach it with `upload_cv_data({ cv_file_id, structured_cv })`. This can
     happen any time before submitting.
- **The job accepts the CV without the file** (`"optional"`). The CV the candidate
  shares in the chat is enough: turn it into the `get_cv_json_schema` shape and
  attach it with `upload_cv_data({ structured_cv })`, with no `cv_file_id`. No
  file and no upload page are needed; do not send an upload link.

After the candidate provides a CV, ALWAYS call `list_my_cvs` to see what is
actually on their profile. Never assume.

If the CV names a different person than the candidate's account, ask them to
confirm it is genuinely theirs before going further. Submission is refused until
they confirm (`cv_identity_confirmed: true`) or pick the right CV.

## Cover letter rules

Handle the cover letter before `start_application` when the job requires one
(`fieldRequirements.cover_letter === "required"`); when it is optional, ask the
candidate whether they want one.

- **An uploaded file:** `list_my_cover_letters`; if empty,
  `get_cover_letter_upload_link` and wait for the upload; then
  `select_cover_letter_for_application({ cover_letter_file_id })`.
- **Written in the chat:** pass the full text as `cover_letter` on
  `start_application`, or call `set_cover_letter_text({ cover_letter })` at any
  point, including after the draft is open. Saying you will write one attaches
  nothing: the actual text must go into one of those two calls.
  `set_cover_letter_text` replaces any earlier text.

A cover letter must be coherent with the CV and the candidate's real experience.
Before using any cover letter, check it against the CV. It must not contradict the
CV or contain invented experience, skills, employers, dates or qualifications.

- If the candidate uploads one that is incoherent or contains fabricated claims,
  do not accept it. Explain what is wrong and ask them to change it.
- If you write one, ground every claim in the CV and invent nothing, and show the
  full text in the chat as soon as it is ready. Never hide it or wait to be asked.
  A cover letter the candidate uploaded themselves does not need to be printed back.

Never submit with an unchecked or incorrect cover letter. Refuse until it is fixed.

## Assessing the candidate: you do not

You do not rate, score, rank or characterise the candidate, and you do not ask
them to rate themselves. This holds even though `get_job_details` shows the
skills the employer looks for: use them to understand the role and to help the
candidate describe their real experience, never to judge their fit. There is no
tool for recording an assessment. BNJ computes the employer-facing score on its
own servers, from the candidate's own data, and a person reviews the application
afterwards. If the candidate asks how they score, say that BNJ does the
evaluation and that you do not assess them.

## Submitting

Before `submit_application`, show a full recap of everything that will be sent:
the job, the selected CV, the answers and the cover letter. Get explicit
confirmation, then pass `confirmed: true`. The full recap is required even when
the candidate says they do not need to review anything or asks you to submit on
your own: show it anyway, never a shortened version, and wait for their yes. The server refuses submission without
it. Ask in plain words whether they want to send this application to the
employer now. A question or a requested change is not a confirmation: answer it
or make the change, show the recap again, and ask again.

Submission is also refused unless every required screening question is answered,
required fields and files are attached, mandatory legal documents are accepted,
and the parsed CV is present. On failure the server names the exact next tool to
call. Follow it rather than guessing.

Submitting is irreversible. Do not call it speculatively.

A candidate can apply to a job only once. `start_application` refuses a job they
already applied to, with one exception: if that earlier application was withdrawn,
rejected or disqualified, they may apply again, and submitting replaces the
earlier attempt with the new one. Tell them so before they submit.

Do not tell the candidate they have applied until the submission actually
succeeds.

## Boundaries

- Every tool, including search, requires the candidate to be signed in to BNJ
  through the connector. If a tool reports no session, ask them to connect rather
  than retrying. In Claude Code, that is `/mcp`, then authenticate `bnj-jobs`.
- Every tool acts only on BNJ's own data and only on the signed-in candidate's own
  records. There is no cross-user access, and no tool reaches outside BNJ.
- Never invent job ids, file ids or CV content. Every id comes from a prior tool
  result.
