# Setting up BraveNewJobs in Claude

You need a Claude **Pro, Max, Team or Enterprise** plan.

There are two ways in. Try the first — it is one file and one upload. If your
Claude does not show a **Plugins** section, use the second.

---

# The quick way — one file

1. Download **`bnj-employer-plugin.zip`**. Keep it zipped.
2. In Claude, open **Customize** in the left sidebar.
   *In Cowork, open the **Cowork** tab first, then Customize.*
3. Go to the **Plugins** tab.
4. Choose the option to **upload a custom plugin file** and pick the zip.
5. When it asks you to sign in to BraveNewJobs, do it, and approve the access.

That is both halves at once — the BraveNewJobs connection and the Odoo know-how.
Skip to **Check it worked**.

> If the upload is refused or you cannot find a Plugins tab, nothing is wrong
> with the file — that section is not available on every plan and app version
> yet. Use the two-step way below, which works everywhere.

---

# The two-step way — works everywhere

Two steps, about two minutes, no files to edit.

---

## Step 1 — Connect BraveNewJobs

This is what lets Claude see your jobs, applications and candidates.

1. Open Claude (the desktop app or claude.ai).
2. Go to **Settings → Connectors**.
3. Click **Add custom connector**.
4. Paste this address:

   ```
   https://employer-mcp.bravenewjobs.com/mcp
   ```

5. Click **Add**, then **Connect**.
6. Sign in with your BraveNewJobs account and approve the access it asks for.

You only do this once. Claude never sees your BNJ password — it receives a token
that you can revoke at any time from the same screen.

> **Team and Enterprise plans:** only an organisation Owner can add the
> connector. Once it is added, everyone else turns it on for themselves from the
> same Connectors screen.

---

## Step 2 — Add the Odoo skill

This teaches Claude how your Odoo integration actually behaves, so it gives you
straight answers instead of guessing.

1. Download **`bnj-odoo-sync-skill.zip`** (attached, or from your BNJ contact).
   Keep it zipped — don't unzip it.
2. In Claude, go to **Settings → Capabilities** and make sure **Code execution**
   is on. Skills need it.
3. Go to **Skills**.
4. Click **+**, choose **Upload a skill**, and pick the zip file.

Claude uses it automatically whenever you talk about Odoo. There is nothing to
switch on per conversation.

---

## Check it worked

Start a new chat and ask:

> Is our Odoo connected, and what is waiting to sync?

You should get your company's name back, when the sync last ran, and a count of
jobs and applications not yet on the other side. If Claude says it has no such
tool, Step 1 did not finish — reopen Connectors and check BraveNewJobs shows as
connected.

---

## What you can now do

Five things, all in plain conversation. You never have to name a tool.

| Ask for | What happens |
|---|---|
| *"Is our Odoo connected, and what is waiting to sync?"* | Reports the connection, when it last ran, and how many jobs and applications are not yet on the other side. Changes nothing. |
| *"Bring our Odoo jobs into BNJ."* | Creates the job positions BNJ does not have, **as drafts**, with their recruitment stages as the BNJ pipeline. |
| *"Bring our Odoo applications into BNJ."* | Creates the applications and the candidates behind them. Do the jobs first — an application needs its job to exist in BNJ. |
| *"Put this job in our Odoo."* | Creates one BNJ job in Odoo, if it is not there already. |
| *"Send this application to Odoo."* | Creates one BNJ application in Odoo, if it is not there already. |

Add *"show me what that would create first"* to any of them for a preview that
writes nothing. Every real run ends with a plain report: what was created, what
was already there, and what was skipped and why. Nothing is skipped silently.

Large histories arrive in batches — Claude will tell you when more remain and
offer to carry on.

### What comes across

Jobs bring their title, description, department, employment type, location,
deadline and stages. Applications bring the stage, when the person applied, their
salary expectation, and — for anyone refused or archived in Odoo — the rejection
with **your own reason and date**, not the date of the import. Candidates bring
name, email, phone, LinkedIn and city, matched on email so one person applying to
four roles stays one person. Custom fields come across as labelled notes, both
the Studio kind and Properties.

### What it never does

Never publishes a job. Never emails anyone. Never runs AI scoring on an imported
application. Never gives an imported candidate a login. Never deletes anything on
either side. Never runs on a schedule — only when you ask.

### The one thing to know before you start

**The sync only ever creates what is missing. It never changes a record that
already exists on the other side.** An edit made after a record has synced does
not travel — in either direction. That is what stops two systems overwriting each
other's work, and it means you decide which platform owns a given record. Your
BNJ contact can walk you through what that means for your setup.

---

## If something does not work

| What you see | What it means |
|---|---|
| "Odoo is not connected for this company" | Connect Odoo under **Integrations** in the BNJ dashboard. Separate from Step 1. |
| "Integrations are not switched on" | Ask BNJ support to enable them for your account. |
| Claude can see jobs but cannot import applications | The connector needs the applications permission. Disconnect and reconnect it in Step 1 to grant it. |
| No **Add custom connector** button | Your plan does not include custom connectors — Pro, Max, Team or Enterprise is required. |
| No **Skills** section | Turn on **Code execution** under Settings → Capabilities first. |
| No **Plugins** tab, or the zip upload is refused | Not every plan and app version has plugin upload yet. Use the two-step way — same result. |
| Your company restricts what can be installed | On Team and Enterprise an administrator can limit plugins and connectors. Ask them to allow BraveNewJobs. |

Anything else: **support@bravenewjobs.com**.
