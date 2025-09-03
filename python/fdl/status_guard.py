import os, time
from dataclasses import dataclass

@dataclass
class GuardCfg:
    enabled: bool = os.getenv("STATUS_GUARD", "0") == "1"
    window_sec: int = int(os.getenv("STATUS_GUARD_WINDOW", "60"))
    trip_errors: int = int(os.getenv("STATUS_GUARD_TRIP", "3"))

class StatusGuard:
    def __init__(self, cfg: GuardCfg | None = None):
        self.cfg = cfg or GuardCfg()
        self.errors: list[float] = []

    def note_error(self):
        now = time.time()
        self.errors.append(now)
        self.errors = [t for t in self.errors if now - t <= self.cfg.window_sec]

    def degraded(self) -> bool:
        if not self.cfg.enabled: 
            return False
        if os.getenv("OPENAI_STATUS", "").lower() == "incident":
            return True
        now = time.time()
        self.errors = [t for t in self.errors if now - t <= self.cfg.window_sec]
        return len(self.errors) >= self.cfg.trip_errors

    def suggest_kwargs(self) -> dict:
        if not self.degraded():
            return {"stream": True}
        # деградация: отключаем стриминг и ужимаем ответ
        return {"stream": False, "max_output_tokens": 800}

# === пример использования в examples/structured_outputs.py ===
# guard = StatusGuard()
# kwargs = guard.suggest_kwargs()
# try:
#     resp = client.responses.create(model="gpt-4o", input=prompt,
#                                    response_format=..., **kwargs)
# except Exception:
#     guard.note_error()
#     # повтор без стрима
#     resp = client.responses.create(model="gpt-4o", input=prompt,
#                                    response_format=..., stream=False)
