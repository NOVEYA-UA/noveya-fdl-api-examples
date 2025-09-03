import re
from typing import Tuple, List

class LightGuard:
    """Minimal pre-processor that flags/blocks disallowed tokens before API calls."""

    def __init__(self, allow=("AZ", "SI", "RЦ"), deny=None):
        self.allow = set(allow)
        self.deny = set(deny or [])
        self.active = True

    def validate_symbol(self, s: str) -> bool:
        return s in self.allow

    def protect(self, text: str) -> Tuple[str, List[str]]:
        findings = []
        lowered = text.lower()
        for neg in self.deny:
            if neg in lowered:
                findings.append(neg)
        if findings:
            return "[LightGuard blocked: disallowed markers detected]", findings
        return text, findings
