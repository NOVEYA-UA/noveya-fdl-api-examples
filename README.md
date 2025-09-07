# NOVEYA • GPT Actions Starter

Этот пакет содержит:
- `openapi.yaml` — спецификация для импорта в **GPT → Configure → Actions → Create new action**
- `fastapi_cors_snippet.py` — фрагмент для включения CORS в FastAPI
- `ACTIONS-GUIDE.md` — пошаговая инструкция

## Быстрый план
1. **Разверните API** из вашего репозитория (есть `Dockerfile` / `run.sh`).
2. Включите CORS (см. `fastapi_cors_snippet.py`).
3. Опубликуйте `openapi.yaml` в GitHub (корень проекта) — получите raw-URL.
4. В конструкторе GPT: **Configure → Actions → Create New Action → Import from URL** и укажите raw-URL.
5. Настройте **Authentication**: API Key (заголовок `X-API-Key`) или OAuth.
6. Нажмите **Test** на каждом эндпоинте; сохраните GPT.
