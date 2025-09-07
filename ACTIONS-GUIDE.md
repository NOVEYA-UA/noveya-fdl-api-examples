# ACTIONS-GUIDE.md — как добавить «Действия» в ваш GPT

## 0) Что понадобится
- Публично доступный HTTPS-домен с вашим API (`gateways.py`).
- Загруженный в репозиторий `openapi.yaml` (эта спецификация).
- Политики: PRIVACY/SECURITY (ссылка нужна при публикации GPT).

## 1) Развернуть API
- Локально: `uvicorn gateways:app --host 0.0.0.0 --port 8000` и пробросить через HTTPS-туннель/хостинг.
- Контейнер: `docker build -t gpt-n7dplus . && docker run -p 8000:8000 gpt-n7dplus`.
- Хостинг любой (Fly/Render/Railway/VM) — главное, чтобы был HTTPS и стабильный URL.

## 2) Включить CORS
Вставьте фрагмент из `fastapi_cors_snippet.py`. Для продакшена лучше ограничить `allow_origins` конкретными доменами.

## 3) Положить openapi.yaml в GitHub
- Коммитите `openapi.yaml` в корень вашего репозитория (или в `/api/`).
- Получите **Raw URL** (например: `https://raw.githubusercontent.com/<org>/<repo>/main/openapi.yaml`).

## 4) Создать Action в GPT
- В ChatGPT → **Explore GPTs → Create → Configure → Actions → Create new action**.
- Нажмите **Import from URL** и вставьте **Raw URL** на `openapi.yaml`.
- Если валидация пройдёт — увидите список эндпоинтов.

## 5) Аутентификация
- Выберите **API Key** → *Header* → **X-API-Key** (как в `openapi.yaml`).  
  Этот ключ будет использоваться вашим GPT для всех пользователей.
- Либо настроить **OAuth** (если вам нужна индивидуальная авторизация пользователей).

## 6) Проверка
- В разделе Actions выберите эндпоинт и нажмите **Run** (внутри конструктора).  
- Затем сохраните GPT и протестируйте запросы в чате.

## Советы
- Ответы API всегда в JSON; используйте чёткие описания `summary`/`operationId` — это помогает модели правильно выбирать эндпоинт.
- Если действия «не видны», проверьте: HTTPS, CORS, корректный `servers.url` и доступность `openapi.yaml` по URL.
