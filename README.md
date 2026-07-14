# Anthropic Certification — Course Workspace

Jupyter + Python-SDK workspace for the **Anthropic CPN (Claude Partner Network)** learning path. One shared `.venv` and `.env` at the root serve every course; each course has its own top-level folder.

> **New here?** Do the [one-time setup](#setup) first. Day to day, the two sections you'll actually use as a prep assistant are the **model cheatsheet** and the **gotchas log** directly below.

## Model cheatsheet — which model, when

| When | Use |
|------|-----|
| **Default** for most exercises | `claude-sonnet-5` (balanced flagship) |
| Lesson needs a **removed param** (`temperature`/`top_p`/`top_k`) or **assistant prefill** | `claude-haiku-4-5-20251001` (still supports them; also fast/cheap for eval loops) |
| Need the **most capable** model | `claude-opus-4-8` |

## Gotchas log — course vs. current models

The course was recorded on older models, so some examples break on today's flagships. Each row is a break we hit and the fix. **Add to this whenever a new one turns up.**

| Symptom | Fix |
|---------|-----|
| **404** on `claude-sonnet-4-0` | Model removed → use `claude-sonnet-5`. |
| `ThinkingBlock has no attribute 'text'` / `content[0]` is wrong | Flagships emit a **ThinkingBlock first** → scan `message.content` for the first block with `.type == "text"` (a `get_text()` helper). |
| **400** on `temperature` / `top_p` / `top_k` | Removed on flagships → use `claude-haiku-4-5-20251001`. |
| **400** on assistant **prefill** (last turn is `assistant`) | Removed on flagships → use Haiku 4.5, or prefer **structured outputs** for clean JSON. |
| **400** `additionalProperties: true is not supported` | Every `object` in a structured-output schema must set `additionalProperties: false`. |
| **400** on thinking `{"type":"enabled","budget_tokens":N}` | Flagships use `thinking={"type":"adaptive"}` + `effort`. Legacy `enabled`+`budget_tokens` **still works on Haiku 4.5** (why the course code runs there). Thinking needs `temperature=1` and can't combine with prefill. |
| Prompt cache never writes (`cache_creation_input_tokens` stays 0) | **Min-to-cache is model-dependent**; course's "1024" is wrong for Haiku. **Haiku 4.5 needs ≥4,096 tokens** cached (Sonnet/Opus 1,024; Fable/Mythos 512). Default TTL is **5 min** (not 1 h); pass `"ttl":"1h"` for the hour tier. |

**Fine as-is:** `stop_sequences` works on all current models.

**Score drift (expected, not a bug):** the course quotes eval scores from a weaker model. On `claude-haiku-4-5` even a naive prompt scores near the ceiling (e.g. "clear and direct" hit **8+** locally vs. the course's 3.92), so per-technique gains look compressed. Don't expect the course's dramatic 2→8 climb.

## Concept notes

- **Tool functions aren't Python-specific.** The course writes handlers in Python, but the contract with Claude is **JSON over HTTP**: Claude sees each tool's **JSON schema** and returns a `tool_use` block with JSON args; your backend can execute *anything* (a DB query, an HTTP call, a shell command) in any language, then returns a `tool_result`. (Separately, **server-side tools** like `web_search` / `code_execution` run on Anthropic's infra — you enable them, you don't implement them.)

## Setup

**One-time — add your API key:**

```powershell
Copy-Item .env.example .env   # then paste your key from https://console.anthropic.com/settings/keys
```

`.env` is git-ignored. `.vscode/settings.json` pins the Jupyter working dir to the repo root, so `load_dotenv()` finds `.env` from any nested folder.

**Run a notebook** — open any `.ipynb` in VS Code and pick the **Python (anthropic-cert)** kernel. (Browser Jupyter also works: `.\.venv\Scripts\Activate.ps1; jupyter notebook`.)

**Recreate the env elsewhere:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m ipykernel install --user --name anthropic-cert --display-name "Python (anthropic-cert)"
```

## Course map

One top-level folder per CPN course:

| Course folder | Status |
|---------------|--------|
| `building-with-the-claude-api/` | ✅ Complete — 9 sections (accessing the API, prompt eval, prompt engineering, tool use, RAG, features, **MCP**, Anthropic apps, agents & workflows) |
| `introduction-to-agent-skills/` | ✅ Complete — 6 flat numbered notebooks |
| `claude-code-in-action/` | ✅ Complete — sectioned |
| `introduction-to-mcp/` | 🚧 In progress |

Notebooks are numbered to match course order (sectioned courses use numbered section subfolders). See each course's own `README.md` for its lesson list.
