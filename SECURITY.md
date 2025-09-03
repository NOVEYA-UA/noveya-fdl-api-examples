# Security guidance

- **Keys**: store `OPENAI_API_KEY` in env vars or a KMS; never commit to VCS.
- **Rotation**: rotate keys regularly; revoke immediately if leaked.
- **Scoping**: use separate keys per agent/subsystem to isolate usage and audit.
- **Telemetry**: log hashed user/session IDs and request fingerprints on your side.
- **Prompt hygiene**: normalize/validate inputs before calling the API (see LightGuard).
- **Data**: avoid sending PII; if needed, pseudonymize and minimize context.