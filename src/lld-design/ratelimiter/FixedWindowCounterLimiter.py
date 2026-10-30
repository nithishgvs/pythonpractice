import time
import threading
from typing import Dict

from Limiter import Limiter
from RateLimitResult import RateLimitResult


class WindowState:
    def __init__(self, window_start_ms: int, count: int):
        self.window_start_ms = window_start_ms
        self.count = count


class FixedWindowCounterLimiter(Limiter):
    def __init__(self, max_requests: int, window_ms: int):
        self.max_requests = max_requests
        self.window_ms = window_ms
        self._windows: Dict[str, WindowState] = {}
        # Protects both the client-window map and each window's mutable state.
        self._lock = threading.Lock()

    def allow(self, client_id: str) -> RateLimitResult:
        # Keep lookup, reset, check, and increment atomic so concurrent calls
        # cannot both consume the same remaining request slot.
        with self._lock:
            now = int(time.time() * 1000)
            window = self._get_or_create_fixed_window_counter(client_id, now)

            if now - window.window_start_ms >= self.window_ms:
                window.window_start_ms = now
                window.count = 0

            if window.count < self.max_requests:
                window.count += 1
                remaining = self.max_requests - window.count
                return RateLimitResult(True, remaining, None)

            retry_after_ms = window.window_start_ms + self.window_ms - now
            return RateLimitResult(False, 0, retry_after_ms)

    def _get_or_create_fixed_window_counter(
        self, client_id: str, now: int
    ) -> WindowState:
        if client_id not in self._windows:
            self._windows[client_id] = WindowState(now, 0)
        return self._windows[client_id]
