{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "fdl_cycle",
  "type": "object",
  "required": [
    "token_id",
    "cycle"
  ],
  "properties": {
    "token_id": {
      "type": "string"
    },
    "cycle": {
      "type": "object",
      "required": [
        "thesis",
        "antithesis",
        "synthesis"
      ],
      "properties": {
        "thesis": {
          "type": "string"
        },
        "antithesis": {
          "type": "string"
        },
        "synthesis": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "metadata": {
      "type": "object",
      "properties": {
        "author": {
          "type": "string"
        },
        "context": {
          "type": "string"
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
