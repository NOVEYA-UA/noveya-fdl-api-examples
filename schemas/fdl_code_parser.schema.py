{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "fdl_code_parse",
  "type": "object",
  "required": [
    "commands"
  ],
  "properties": {
    "commands": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "code",
          "action",
          "domain",
          "intent",
          "normalized",
          "safety"
        ],
        "properties": {
          "code": {
            "type": "string"
          },
          "action": {
            "type": "string"
          },
          "domain": {
            "type": "string"
          },
          "intent": {
            "type": "string"
          },
          "tokens": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "tonality": {
            "type": "string"
          },
          "symbols": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "normalized": {
            "type": "string"
          },
          "safety": {
            "type": "object",
            "required": [
              "allowed"
            ],
            "properties": {
              "allowed": {
                "type": "boolean"
              },
              "reason": {
                "type": "string"
              }
            },
            "additionalProperties": false
          }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
