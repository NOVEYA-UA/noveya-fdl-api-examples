# Structured Outputs (Responses API) — strict JSON Schema normalization
import json
import pathlib
from openai import OpenAI

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCHEMA = json.loads((ROOT / "schemas" / "fdl_code_parser.schema.json").read_text("utf-8"))
RAW = (ROOT / "examples" / "raw" / "fdl_block.txt").read_text("utf-8")

client = OpenAI()

prompt = (
    "Разбери символический блок Σ-FDL и верни строгий JSON по схеме. "
    "Каждую строку-код нормализуй в объект с action/domain/intent, описанием 'normalized' "
    "и safety.allowed/reason. Неизвестные — allowed=false.\n\nВход:\n" + RAW
)

resp = client.responses.create(
    model="gpt-4o",
    input=prompt,
    response_format={
        "type": "json_schema",
        "json_schema": {"name": "fdl_code_parse", "schema": SCHEMA, "strict": True},
    },
)

parsed = resp.output_parsed  # dict per JSON schema
print(json.dumps(parsed, ensure_ascii=False, indent=2))
