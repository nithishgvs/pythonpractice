import time
import threading
from collections import deque
from typing import Dict

from Limiter import Limiter
from RateLimitResult import RateLimitResult


class RequestLog:
    def __init__(self, timestamps: deque):
        self.timestamps = timestamps


class SlidingWindowLogLimiter(Limiter):

    def __init__(self, max_requests: int, window_ms: int):
        self._max_requests = max_requests
        self._window_ms = window_ms
        self._logs: Dict[str, RequestLog] = {}
        self._lock = threading.Lock()

    def allow(self, client_id: str) -> RateLimitResult:
        # Keep pruning, checking, and appending atomic for concurrent callers.
        with self._lock:
            log = self._get_or_create_log(client_id)
            now = int(time.time() * 1000)
            cutoff = now - self._window_ms

            while log.timestamps and log.timestamps[0] < cutoff:
                log.timestamps.popleft()

            if len(log.timestamps) < self._max_requests:
                log.timestamps.append(now)
                remaining = self._max_requests - len(log.timestamps)
                return RateLimitResult(True, remaining, None)
            oldest_timestamp = log.timestamps[0]
            retry_after_ms = (oldest_timestamp + self._window_ms) - now
            return RateLimitResult(False, 0, retry_after_ms)

    def _get_or_create_log(self, client_id) -> RequestLog:
        if client_id not in self._logs:
            self._logs[client_id] = RequestLog(deque())
        return self._logs[client_id]
