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

  ## Design decisions (confirmed with OpenAI)

- **Baseline (one-shot normalization/analysis):** Responses API + `response_format: { type: "json_schema", strict: true }`.
- **Orchestration & multi-tool:** Function Calling with `tools`, explicit `tool_choice`, `strict: true`.
- **Schema practicality (strict mode):** target depth 3–5 levels; typical output size ~20–50 KB. For deeper/variable data, split into modules or group rare/experimental fields under `"experimental": {...}`.
- **Forward compatibility:** new fields (`glyph_map`, `musical_key`, `astro_bindings`) are optional or placed in `"experimental"` to preserve backward compatibility.
