# Design decisions (confirmed with OpenAI)

This document captures baseline decisions for Σ-FDL integrations in **NOVEYA-FDL-API-Examples**.

## Baseline patterns
- **One-shot normalization / analysis:** use **Responses API** with
  `response_format: { type: "json_schema", strict: true }`.
- **Orchestration / multi-tool flows:** use **Function Calling** with `tools`,
  explicit **`tool_choice`**, and **`strict: true`** at the function level.
- Treat these as defaults in the examples and README.

## JSON Schema practicality (strict mode)
- Target depth **3–5 levels** of nesting for best reliability.
- Typical output size target **~20–50 KB** per response.
- For deeper / highly variable structures:
  - split into **modular** schemas/outputs, and/or
  - place rarely used or experimental attributes under `"experimental": { ... }`.
- Keep **optional** fields truly optional; avoid breaking backward compatibility.

## Forward compatibility
- New fields such as `glyph_map`, `musical_key`, `astro_bindings`:
  - add them as **optional** or inside `"experimental"`;
  - document intended types/enums and provide small samples.

## Model/context guidelines
- Ensure your **prompt + schema + expected output** fits into the model’s context window.
- Use `max_output_tokens` to bound outputs where appropriate.
- Validate against schema on the client side; on failure, retry with a reduced prompt or segmented tasks.

## Degradation & resilience (optional)
- During UI/product incidents, prefer **Responses API** with **non-streaming** fallbacks.
- Consider a thin local pre-processor (**LightGuard**) for input hygiene and early blocking of undesired tokens.
- For demos/CI, you may add an optional `status-guard` (env-flag) to turn off streaming and reduce output size when repeated transport errors are observed.

## Testing strategy
- Maintain **golden samples**:
  - **Input** text blocks (symbolic Σ-FDL snippets).
  - **Expected** normalized JSON per schema.
- Add **schema validation** in CI (e.g. Python `jsonschema`, Node `ajv`) against both examples and golden outputs.
- Prefer **small, deterministic** examples; update goldens only when the schema changes.

## Security & privacy
- Store secrets in environment variables or a secrets manager; rotate keys regularly.
- Separate API keys per agent/subsystem for auditability.
- Avoid sending PII; if necessary, pseudonymize and minimize context.
