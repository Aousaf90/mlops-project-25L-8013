# Git & MLOps Assignment 1 Report

**Course:** MLOps  
**Assignment:** Version Control with Git, GitHub, and Visual Studio Code  
**Student ID:** 25L-8013  
**Deadline:** 9/9/2026 11:55 PM  

**Public GitHub Repository:**  
https://github.com/Aousaf90/mlops-project-25L-8013.git

---

## How to use this document

1. Capture the required screenshots from VS Code (Terminal / Source Control / Merge editor).
2. Paste each screenshot under the matching **Screenshot placeholder** below.
3. Export this file to Word or PDF as:  
   `Git_MLOps_Report_25L-8013.docx` or `Git_MLOps_Report_25L-8013.pdf`
4. Submit the report **and** the public repository link.

---

## 1. Introduction & Objective

This assignment builds a foundational MLOps workflow for a breast cancer classification project. The goals were to:

- Separate **source code**, **datasets**, and **model artifacts** cleanly
- Version only lightweight, reproducible files with Git and GitHub
- Practice staging, resets, branching, merge conflicts, history inspection, and stash

Student ID **25L-8013** is used in the repository name, branch names, training script filename, and commit messages.

---

## 2. Part 1 — Environment Configuration & Repository Initialization

### 2.1 Repository structure

The project uses the following layout:

```text
├── data/                          # Raw dataset (ignored by Git)
├── src/
│   └── train_25L8013.py           # Training script
├── model/                         # Trained model output (ignored by Git)
├── docs/
│   └── Git_MLOps_Report_25L-8013.md
├── .gitignore
├── requirements.txt
└── README.md
```

### 2.2 Model training script

`src/train_25L8013.py` performs:

1. Loads the dataset from `data/`
2. Trains a Scikit-Learn Logistic Regression model (with a preprocessing scaler in a pipeline)
3. Saves the trained model to `model/` as a `.joblib` file

### 2.3 Reproducibility

- `requirements.txt` lists the environment dependencies
- `README.md` documents install and run commands from the repository root

### 2.4 GitHub repository

- Repository name: `mlops-project-25L-8013`
- Remote URL: https://github.com/Aousaf90/mlops-project-25L-8013.git
- Default branch: `main`

**Screenshot placeholder — Git identity / clone / initial remote setup (optional)**  
*(Paste VS Code terminal screenshot here showing Git user config and/or successful clone.)*

> ![Screenshot: Git setup / clone](screenshots/01_git_setup.png)

---

## 3. Part 2 — Managing MLOps Artifacts with `.gitignore`

### 3.1 Purpose

Raw datasets and heavy model binaries must not be pushed to GitHub. Only source code and configuration files are versioned.

### 3.2 `.gitignore` rules

The root `.gitignore` excludes:

- `data/` contents (raw datasets)
- `model/` contents (serialized models)
- Virtual environments (`venv/`)
- Editor / OS noise (e.g. `.vscode/`, `.DS_Store`)
- *(Add any extra rules you configured, e.g. `__pycache__/`, `*.pkl`, `*.h5`, if present)*

### 3.3 Verification

After placing data/model files locally, `git status` should **not** list them as untracked. Only code and config files should appear for commit.

**Screenshot 1 (required)** — `.gitignore` contents **and** repository status proving large data/model files are excluded  

> ![Screenshot: .gitignore and git status](screenshots/02_gitignore_and_status.png)

**Notes for this screenshot:**
- Show the open `.gitignore` file in the editor
- Show Terminal or Source Control with `git status` where `data/` and `model/` artifacts do not appear as untracked

---

## 4. Part 3 — Staging, Snapshots, and Reset Operations

### 4.1 Iterative experimentation

A hyperparameter (or related training setting) was added/modified in `src/train_25L8013.py`. Uncommitted changes were inspected with VS Code Diff / `git diff`.

### 4.2 Soft and hard resets

Workflow practiced:

1. Modify the training script
2. Stage the change (`git add`)
3. **Soft reset** — unstage while keeping file edits (`git reset` / `git reset --soft`)
4. **Hard reset** — discard local changes back to last commit (`git reset --hard`) *(use carefully)*

**Screenshot 2 (required)** — Terminal or Source Control showing effects of soft and hard resets  

> ![Screenshot: soft and hard resets](screenshots/03_soft_hard_reset.png)

**Notes for this screenshot:**
- Capture status before/after soft reset (changes remain, staging cleared)
- Capture status after hard reset (working tree matches last commit)

---

## 5. Part 4 — Branching, Collaboration, and Conflict Resolution

### 5.1 Feature branches

| Branch | Purpose |
|--------|---------|
| `feature-preprocessing-25L8013` | Data normalization / preprocessing change |
| `feature-tuning-25L8013` | Alternative feature-scaling / tuning change |

Both branches modified the **same line** in `src/train_25L8013.py` differently, which produced a merge conflict when integrating.

### 5.2 Conflict simulation and resolution

1. Create/push both feature branches
2. Merge one branch into `main`, then merge the second → conflict markers appear
3. Resolve in VS Code merge editor (`<<<<<<<`, `=======`, `>>>>>>>`)
4. Stage the resolved file, complete the merge commit, push `main`

**Screenshot 3 (required)** — VS Code merge conflict interface showing conflict markers  

> ![Screenshot: merge conflict in VS Code](screenshots/04_merge_conflict.png)

**Notes for this screenshot:**
- Capture the conflicted `train_25L8013.py` with markers visible, **or** the VS Code “Accept Current / Incoming / Both” merge UI

---

## 6. Part 5 — Inspection and History Management

### 6.1 Commit visualization

Commands used (or equivalent VS Code Git Graph / Timeline):

```bash
git log --oneline --graph --all
```

### 6.2 Tracking file evolution

```bash
git log --follow -- src/train_25L8013.py
```

### 6.3 Context switching with stash

```bash
git stash
git stash list
git stash pop
```

**Screenshot 4 (required)** — Final commit history graph after successful merge  

> ![Screenshot: commit history graph](screenshots/05_commit_graph.png)

**Notes for this screenshot:**
- Prefer `git log --oneline --graph --all` in the VS Code terminal, or a Git Graph extension view
- The graph should show feature branches and the merge into `main`

**Screenshot placeholder — stash / follow (optional)**  

> ![Screenshot: git stash or git log --follow](screenshots/06_stash_or_follow.png)

---

## 7. Submission Checklist Evidence

| # | Requirement | Location in this report |
|---|-------------|-------------------------|
| 1 | `.gitignore` + status proving data/models excluded | Section 3 — Screenshot 1 |
| 2 | Soft and hard reset effects | Section 4 — Screenshot 2 |
| 3 | Merge conflict UI with markers | Section 5 — Screenshot 3 |
| 4 | Final commit history graph after merge | Section 6 — Screenshot 4 |
| 5 | Live public GitHub URL with student ID | Below |

### 7.1 Public repository link

**https://github.com/Aousaf90/mlops-project-25L-8013**

---

## 8. Repository Evaluation Criteria (Self-check)

| Criterion | Status / Notes |
|-----------|----------------|
| Clean separation of code, data, and models | `src/`, `data/`, `model/` present |
| `.gitignore` blocks raw data and model binaries | No `.csv` / `.pkl` / `.joblib` on GitHub |
| Complete `requirements.txt` | Present at repo root |
| Clear instructional `README.md` | Install + run commands documented |
| Training script runs and writes model to `model/` | `python src/train_25L8013.py` |

---

## 9. Conclusion

This assignment practiced a realistic MLOps Git workflow: ignore heavy artifacts, keep the remote repository lightweight, experiment safely with staging and resets, collaborate via feature branches, resolve merge conflicts in VS Code, and inspect history with logging and stash.

---

## Appendix A — Useful commands reference

```bash
# Status / diff
git status
git diff

# Stage & commit
git add .
git commit -m "25L-8013: descriptive message"

# Soft / hard reset
git reset HEAD~1          # soft-style uncommit keeping changes (or: git reset --soft HEAD~1)
git reset                 # unstage
git reset --hard HEAD     # discard local changes

# Branches
git checkout -b feature-preprocessing-25L8013
git checkout -b feature-tuning-25L8013
git checkout main
git merge feature-preprocessing-25L8013
git merge feature-tuning-25L8013

# History / stash
git log --oneline --graph --all
git log --follow -- src/train_25L8013.py
git stash
git stash pop

# Push
git push -u origin HEAD
git push origin main
```

## Appendix B — Screenshot file naming (suggested)

Create a folder `docs/screenshots/` and save images as:

| File | Content |
|------|---------|
| `01_git_setup.png` | Git config / clone (optional) |
| `02_gitignore_and_status.png` | `.gitignore` + `git status` |
| `03_soft_hard_reset.png` | Soft / hard reset |
| `04_merge_conflict.png` | Conflict markers in VS Code |
| `05_commit_graph.png` | Final merge history graph |
| `06_stash_or_follow.png` | Stash or `--follow` (optional) |

After pasting images into Word/PDF, you may delete unused placeholders.
