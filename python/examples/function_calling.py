# Function Calling (Chat Completions) — forced tool call with strict params
import json
import pathlib
from openai import OpenAI

ROOT = pathlib.Path(__file__).resolve().parents[2]
RAW = (ROOT / "examples" / "raw" / "fdl_block.txt").read_text("utf-8")

client = OpenAI()

tools = [{
    "type": "function",
    "function": {
        "name": "parse_fdl_codes",
        "description": "Normalize Σ-FDL codes into commands[].",
        "parameters": {
            "type": "object",
            "properties": {
                "commands": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["code","action","domain","intent","normalized","safety"],
                        "properties": {
                            "code": {"type": "string"},
                            "action": {"type": "string"},
                            "domain": {"type": "string"},
                            "intent": {"type": "string"},
                            "tokens": {"type": "array", "items": {"type": "string"}},
                            "tonality": {"type": "string"},
                            "symbols": {"type": "array", "items": {"type": "string"}},
                            "normalized": {"type": "string"},
                            "safety": {
                                "type": "object",
                                "required": ["allowed"],
                                "properties": {
                                    "allowed": {"type": "boolean"},
                                    "reason": {"type": "string"}
                                },
                                "additionalProperties": False
                            }
                        },
                        "additionalProperties": False
                    }
                }
            },
            "required": ["commands"],
            "additionalProperties": False
        },
        "strict": True
    }
}]

system_msg = (
    "Ты — Σ-FDL parser. Возвращай только аргументы функции строго по параметрам."
)

user_msg = (
    "Разбери блок на список commands[]. Для неизвестных кодов — allowed=false.\nВход:\n" + RAW
)

resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_msg},
    ],
    tools=tools,
    tool_choice={"type": "function", "function": {"name": "parse_fdl_codes"}},
)

call = resp.choices[0].message.tool_calls[0]
args = json.loads(call.function.arguments)
print(json.dumps(args, ensure_ascii=False, indent=2))
