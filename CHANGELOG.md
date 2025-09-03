# Changelog

## v0.1.0 — Initial public companion
### Added
- `schemas/fdl_cycle.schema.json` — strict cycle schema (thesis/antithesis/synthesis).
- `schemas/fdl_code_parser.schema.json` — strict normalized commands schema.
- Python examples: `python/examples/structured_outputs.py`, `python/examples/function_calling.py`.
- Node examples: `node/examples/structuredOutputs.mjs`, `node/examples/functionCalling.mjs`.
- Light pre-processor: `python/fdl/light_guard.py`.
- Design doc: `README.design-decisions.md` (confirmed patterns).
- Issue templates & PR template under `.github/`.

### Notes
- SemVer for schemas: add optional fields → **minor**; change required/types → **major**.

## v0.1.1 — Schema refinements
### Changed
- `fdl_code_parser.schema.json`: added `enum` constraints for `action`, `domain`, `intent`; extended `safety` with `reason_code` (enum) and `reason_text` (free text). Optional `category` for experimental entries.
- `fdl_cycle.schema.json`: optional `cycle_id`, `timestamp` (ISO 8601), and `experimental` block (`glyph_map`, `musical_key`, `astro_bindings`).

### Notes
- Backward compatibility is preserved (existing payloads still validate: `safety.reason` remains optional, new fields are optional).
