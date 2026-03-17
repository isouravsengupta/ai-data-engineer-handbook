# Update AI Data Engineer Gita Workflow

Run the full workflow to synchronize the Canvas document with the repository and finalize the update.

## Step 1 — Sync Canvas → Repository

Read the Canvas document titled **AI Data Engineer Gita** and synchronize the content into the repository.

Rules:

- Map Canvas sections to files inside the `/book` directory.
- Example mappings:

Master Roadmap -> book/00_master_roadmap.md  
Setup & Installation -> book/01_python_programming/00_setup_installation.md  
Python Roadmap -> book/01_python_programming/01_python_roadmap.md  
Python Basics -> book/01_python_programming/02_python_basics.md  
Lists -> book/01_python_programming/03_lists.md  

- If a file exists, overwrite it.
- If a file does not exist, create it in the appropriate folder.
- Do not modify files outside `/book`.

Before committing show a short summary of updated files.

Commit with message:

sync: update book content from Canvas (AI Data Engineer Gita)

Push changes to:

origin/main

---

## Step 2 — Pull Latest Changes Locally

Run:

git pull origin main

---

## Step 3 — Run Checks

If tests exist, run them.

Example:

pytest

If notebooks exist, execute them:

jupyter nbconvert --execute notebooks/*.ipynb --to notebook --inplace

---

## Step 4 — Stage Local Fixes

If any fixes were made locally:

git add .

---

## Step 5 — Commit Local Refinements

Commit message format:

chore: refine chapter after sync

Command:

git commit -m "chore: refine chapter after sync"

---

## Step 6 — Push Final Changes

Push the finalized version:

git push origin main

---

## Step 7 — Print Progress Summary

Display the files updated and suggest a short progress post:

"I updated a chapter in the AI Data Engineer Gita — deep dive on <topic>.  
Repo: https://github.com/<username>/ai-data-engineer-handbook"