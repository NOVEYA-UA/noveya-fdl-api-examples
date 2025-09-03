# NOVEYA-FDL-API-Examples

Production-ready examples for integrating **Σ-FDL** symbolic codes and cycles with the **OpenAI API** using:

- **Structured Outputs** (Responses API with JSON Schema, `strict:true`)
- **Function Calling** (Chat Completions with `tools` + `tool_choice`)
- Optional **LightGuard** pre-processor for input hygiene

Companion repo for **NOVEYA**. MIT licensed.

## Quick start

### Python
```bash
cd python
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...  # set your key
python examples/structured_outputs.py
python examples/function_calling.py
```

### Node.js (ESM)
```bash
cd node
npm i
export OPENAI_API_KEY=sk-...
npm run so
npm run fc
```

## What’s inside
- `schemas/fdl_cycle.schema.json` — strict schema for FDL cycle
- `schemas/fdl_code_parser.schema.json` — strict schema for normalizing symbolic codes (`commands[]`)
- `python/examples` & `node/examples` — runnable examples
- `python/fdl/light_guard.py` — lightweight pre-processor