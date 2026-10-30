from typing import Optional


class RateLimitResult:
    def __init__(self, allowed: int, remaining: int, retry_after_ms: Optional[int]):
        self.allowed = allowed
        self.remaining = remaining
        self.retry_after_ms = retry_after_ms

    def is_allowed(self) -> bool:
        return self.allowed

    def get_remaining(self) -> int:
        return self.remaining

    def get_retry_after_ms(self) -> Optional[int]:
        return self.retry_after_ms
