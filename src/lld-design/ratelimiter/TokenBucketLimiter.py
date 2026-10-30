import time
import threading
from typing import Dict

from Limiter import Limiter
from RateLimitResult import RateLimitResult


class TokenBucket:
    def __init__(self, tokens: float, last_refill_time: int):
        self.tokens = tokens
        self.last_refill_time = last_refill_time


class TokenBucketLimiter(Limiter):

    def __init__(self, capacity: int, refill_rate_per_second: int):
        self._capacity = capacity
        self._refill_rate_per_second = refill_rate_per_second
        self._buckets: Dict[str, TokenBucket] = {}
        self._lock = threading.Lock()

    def allow(self, client_id: str) -> RateLimitResult:
        # Bucket lookup, refill, and token consumption must be one atomic step.
        with self._lock:
            bucket = self._get_or_create_bucket(client_id)
            now = int(time.time() * 1000)
            elapsed = now - bucket.last_refill_time
            tokens_to_add = (elapsed * self._refill_rate_per_second) / 1000
            bucket.tokens = min(self._capacity, bucket.tokens + tokens_to_add)
            bucket.last_refill_time = now

            if bucket.tokens >= 1:
                bucket.tokens -= 1
                remaining = int(bucket.tokens)
                return RateLimitResult(True, remaining, None)
            tokens_needed = 1 - bucket.tokens
            retry_after_ms = int(
                (tokens_needed * 1000) / self._refill_rate_per_second + 0.999
            )
            return RateLimitResult(False, 0, retry_after_ms)

    def _get_or_create_bucket(self, client_id):
        if client_id not in self._buckets:
            self._buckets[client_id] = TokenBucket(self._capacity, int(time.time() * 1000))
        return self._buckets[client_id]
