# Anthropic Certification — Course Workspace

Environment for the Anthropic certification course exercises (Python SDK + Jupyter).

## Course vs. current models — adaptations log

The course was recorded against older models, so several examples break on today's flagship models. This is a **running list** of every deprecation/behavior change we've hit and the fix we apply — add to it whenever a new one turns up.

| # | Symptom | Cause | Fix |
|---|---------|-------|-----|
| 1 | `NotFoundError` **404** on `claude-sonnet-4-0` | Model removed | Use `claude-sonnet-5` (balanced flagship default) |
| 2 | `AttributeError: 'ThinkingBlock' object has no attribute 'text'` (or `content[0]` isn't the text) | Flagship models emit a **ThinkingBlock first**, so `message.content[0].text` grabs the wrong block | Use a `get_text()` helper that scans `message.content` for the first block with `.type == "text"` |
| 3 | **400** when passing `temperature` (also `top_p` / `top_k`) | These sampling params were **removed** on flagship models (Sonnet 5, Opus 4.7/4.8, Fable 5) | Use `claude-haiku-4-5-20251001`, which still supports them |
| 4 | **400** on assistant-message **prefilling** (last turn is `assistant`) | Last-assistant-turn prefill was **removed** on flagship models | Use `claude-haiku-4-5-20251001` (still supports prefill). Prefer **structured outputs** on flagships when you just need clean JSON |
| 5 | **400** `additionalProperties: true is not supported` (structured outputs) | Schema constraint tightened | Every `object` in the JSON schema must set `additionalProperties: false`; give free-form fields a concrete shape |

**Not affected:** `stop_sequences` works on all current models.

**Capability drift (not an error, but expect it):** the course quotes eval scores from an older, weaker model. On today's `claude-haiku-4-5`, even a *naive* prompt already scores high (e.g. the prompt-engineering section's "clear and direct" step landed **8+** locally vs. the course's 3.92). The techniques still help *relatively*, but absolute scores start near the ceiling, so per-technique gains look compressed (small bumps, occasional noise). Don't expect the course's dramatic 2→8 climb.

**Model cheatsheet:** default `claude-sonnet-5` (balanced flagship) · `claude-haiku-4-5-20251001` (when a lesson needs a *removed* param or prefill — also fast/cheap for eval loops) · `claude-opus-4-8` (most capable).

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
