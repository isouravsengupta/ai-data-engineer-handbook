# Resume Templates (LaTeX-First)

📄 File: `book/20_resume_linkedin/01_resume_templates.md`

This chapter assumes you **build and maintain your resume in LaTeX**. Plain-text structure examples are included for drafting content, but **the canonical resume should be `.tex` → PDF`.

---

## Download-ready template (in this repo)

A **full sample layout** (modeled after professional Lead Data Engineer and Data \& AI Engineer resumes) lives **directly in this folder** (no `latex_template` subfolder):

| Path | Purpose |
|------|---------|
| `ai_data_engineer_resume.tex` | Copy, edit placeholders, compile to PDF |
| `RESUME_LATEX_README.md` | Overleaf link, local compile commands |

**Edit on the web**: open **[Overleaf](https://www.overleaf.com)** → upload `ai_data_engineer_resume.tex` → **Recompile** → download PDF.

---

## 1 — Why Everyone Should Use LaTeX Here

* **Reproducibility**: Same input always produces the same layout (unlike WYSIWYG drift).
* **Git-friendly**: Review resume changes in pull requests like code.
* **Multiple targets**: Maintain one `.tex`; swap a macro or `\\input{skills-ml.tex}` for role-specific variants.
* **Standard among top engineers**: Common in research and strong SWE circles — appropriate for **AI Data Engineer** branding.

**Non-negotiable for this Gita**: Store `resume.tex` (or project folder) in your **portfolio repo** next to projects.

---

## 2 — Tools

| Tool | Best for |
| ---- | -------- |
| **[Overleaf](https://www.overleaf.com/)** | Zero install, templates, share link, history |
| **TeX Live** (Linux/Windows) / **MacTeX** (macOS) | Local builds, `latexmk`, CI (e.g. compile PDF in GitHub Actions) |
| **VS Code + LaTeX Workshop** | Edit `.tex` locally with preview and SyncTeX |

**Compile command** (typical):

```bash
# From directory containing resume.tex
latexmk -pdf resume.tex
# or
pdflatex resume.tex
```

---

## 3 — Recommended LaTeX Resume Templates (Start Here)

Pick **one** simple, ATS-friendly class — avoid heavy graphics.

| Template / repo | Notes |
| --------------- | ----- |
| **[Awesome-CV](https://github.com/posquit0/Alexander-Wilhelm-Awesome-CV)** | Very popular; clean sections; tweak colors minimally for ATS |
| **[Jake’s Resume](https://github.com/jakegut/resume)** | Minimal, one column — excellent for ATS |
| **[moderncv](https://ctan.org/pkg/moderncv)** | Classic CV style; `casual` or `banking` variants |
| **Overleaf gallery** | Search “software engineer resume” — choose **single column**, **minimal** |

**ATS rule**: Prefer **one column**, **standard headings** (`Experience`, `Education`, `Skills`), **selectable text** in PDF (copy-paste a line in a PDF reader to verify).

---

## 4 — Minimal Starter Skeleton (AI Data Engineer)

Use this as a **structure** if you are not using a template yet. Adjust packages to match your TeX distribution.

```latex
% resume.tex — minimal skeleton (comment every non-obvious line)
\documentclass[11pt,a4paper]{article}

% Narrow margins; common for one-page resumes
\usepackage[margin=0.6in]{geometry}
\usepackage{enumitem}   % Tighten bullet lists
\usepackage{hyperref}   % Clickable email (use muted color for print)
\hypersetup{colorlinks=true, linkcolor=black, urlcolor=blue}

% No paragraph indent; small gap between paragraphs
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}

\begin{document}

% --- Header ---
{\LARGE \textbf{Your Name}} \hfill City, Country \\
\href{mailto:you@email.com}{you@email.com} $|$ \href{https://linkedin.com/in/you}{linkedin.com/in/you} $|$ \href{https://github.com/you}{github.com/you}

% --- Summary ---
\section*{Summary}
AI Data Engineer with experience building batch and streaming pipelines, lakehouse storage, and RAG-style retrieval systems. Strong in Python, SQL, and Spark.

% --- Experience ---
\section*{Experience}
\textbf{Company Name} \hfill 2022 -- Present \\
\textit{Senior AI Data Engineer}
\begin{itemize}[noitemsep, topsep=2pt]
  \item Built Spark pipelines processing \textbf{10\,TB/day}; cut job runtime by \textbf{40\%} via partition tuning and broadcast joins.
  \item Shipped RAG retrieval service; \textbf{99.9\%} availability; sub-\textbf{200\,ms} p95 latency at peak.
\end{itemize}

% --- Projects ---
\section*{Projects}
\textbf{Vector search + RAG} (GitHub) --- Chunking, embeddings, FAISS/Qdrant, FastAPI, evaluation with RAGAS.

% --- Skills ---
\section*{Skills}
Python, SQL, Spark, Kafka, dbt, Parquet/Delta, Docker, AWS, PyTorch (basics), vector DBs, LangChain.

% --- Education ---
\section*{Education}
\textbf{B.S. Computer Science}, University Name \hfill Year

\end{document}
```

**Line-by-line notes**:

* `\geometry` — controls page margins; tune so everything fits **one page** for early career.
* `\href` — mailto and URLs; keep URLs short or use clean slugs.
* `\textbf` — bold numbers so impact stands out when skimmed.
* `noitemsep` — denser bullets; more content per page without clutter.
* `\,` in `10\,TB` — thin space between number and unit (typographic detail).

---

## 5 — Plain-Text Outline (Draft Before LaTeX)

Use this to **brainstorm bullets**, then paste into your `.tex`:

```
JANE DOE
LinkedIn | GitHub | jane@email.com

SUMMARY
AI Data Engineer with 5 years building scalable data pipelines...

EXPERIENCE
Senior AI Data Engineer | Company X | 2022–Present
• Built RAG pipeline serving 1M queries/day, 99.9% uptime
• Designed feature store reducing training data prep time by 60%
• Led migration of batch pipelines to Spark, 3x throughput

PROJECTS
• Vector Search Engine (GitHub) — Semantic search over 1M docs
• RAG Pipeline (GitHub) — E2E RAG with evaluation

SKILLS
Python, Spark, Kafka, SQL, PyTorch, RAG, Vector DBs
```

---

## 6 — Action Verbs

* Built, Designed, Led, Optimized, Reduced, Scaled
* Implemented, Migrated, Automated, Deployed

---

## 7 — ATS + LaTeX Checklist

* [ ] PDF text is **selectable** (not a screenshot)
* [ ] Section titles match norms: **Experience**, **Education**, **Skills**
* [ ] **One column** (or very simple two-column with skills sidebar only if tested)
* [ ] File name: `Firstname_Lastname_AI_Data_Engineer.pdf`
* [ ] Spell out **Apache Spark** once if space allows, then **Spark**

---

## Key Takeaways

* **Build your resume in LaTeX** — version control, consistency, professional PDF
* Use **simple, one-column** templates for ATS; compile with `latexmk` or Overleaf
* Draft bullets in plain text → **paste into `.tex`**
* Keep **one page** until you have strong reason for two

---

## Next Chapter

Proceed to: **21_interview_preparation**
