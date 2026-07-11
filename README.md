# Anthropic Certification — Course Workspace

Environment for the Anthropic certification course exercises (Python SDK + Jupyter).

## What's set up

- **`.venv/`** — Python 3.13 virtual environment with `anthropic`, `python-dotenv`, `jupyter`, `ipykernel`
- **Jupyter kernel** — registered as **Python (anthropic-cert)**
- **`getting-started.ipynb`** — walks through the four "Getting Started" steps
- **`.env.example`** — template for your API key

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

Then open `getting-started.ipynb` and confirm the kernel (top-right) is **Python (anthropic-cert)**.

> Prefer VS Code? Just open the folder, open the `.ipynb`, and pick the **Python (anthropic-cert)** kernel — no need to launch Jupyter in a browser.

## Recreate the environment elsewhere

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m ipykernel install --user --name anthropic-cert --display-name "Python (anthropic-cert)"
```
