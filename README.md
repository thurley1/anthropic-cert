# Anthropic Certification — Course Workspace

Environment for the Anthropic certification course exercises (Python SDK + Jupyter).

## What's set up

- **`.venv/`** — Python 3.13 virtual environment with `anthropic`, `python-dotenv`, `jupyter`, `ipykernel`
- **Jupyter kernel** — registered as **Python (anthropic-cert)**
- **`.env.example`** — template for your API key
- **Section folders** — notebooks are organized by course section (see below)

## Folder structure

This repo holds work from the **Claude Partner Network** learning path — one top-level folder per course. A single shared `.venv` and `.env` at the repo root serve every course.

| Course folder | CPN course |
|---------------|------------|
| `building-with-the-claude-api/` | Building with the Claude API |
| `introduction-to-agent-skills/` | Introduction to Agent Skills |
| `introduction-to-mcp/` | Introduction to Model Context Protocol |
| `claude-code-in-action/` | Claude Code in Action |

Within `building-with-the-claude-api/`, notebooks are grouped by course section, numbered to match the course order:

| Section folder | Course section |
|----------------|----------------|
| `01-accessing-the-api/` | Accessing Claude with the API (requests, multi-turn, system prompts, temperature, streaming) |
| `02-prompt-evaluation/` | Prompt evaluation |
| `03-prompt-engineering/` | Prompt engineering techniques |
| `04-tool-use/` | Tool use with Claude |
| `05-rag/` | RAG and Agentic Search |
| `06-features/` | Features of Claude |
| `07-mcp/` | Model Context Protocol |
| `08-anthropic-apps/` | Anthropic apps — Claude Code and computer use |
| `09-agents-and-workflows/` | Agents and workflows |

`.env`, `requirements.txt`, and this README stay at the repo root. `.vscode/settings.json` pins the Jupyter working directory to the repo root so `load_dotenv()` finds `.env` from any course/section folder, however deeply nested.

## One-time: add your API key

1. Get a key at https://console.anthropic.com/settings/keys
2. Copy `.env.example` to `.env`
3. Paste your key into `.env` (this file is git-ignored, so it never gets committed)

```powershell
Copy-Item .env.example .env
```

## Launch Jupyter

```powershell
.\.venv\Scripts\Activate.ps1
jupyter notebook
```

Then open a notebook (e.g. `building-with-the-claude-api/01-accessing-the-api/01-getting-started.ipynb`) and confirm the kernel (top-right) is **Python (anthropic-cert)**.

> Prefer VS Code? Just open the folder, open the `.ipynb`, and pick the **Python (anthropic-cert)** kernel — no need to launch Jupyter in a browser.

## Recreate the environment elsewhere

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m ipykernel install --user --name anthropic-cert --display-name "Python (anthropic-cert)"
```
