import threading
import time
from concurrent.futures import ThreadPoolExecutor


class TokenBucketRateLimiter:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = self.capacity
        self.last_refill_time = time.monotonic()
        self.lock = threading.Lock()

    def refill(self):
        now = time.monotonic()
        elapsed = now - self.last_refill_time
        tokens_to_add = elapsed * self.refill_rate

        if tokens_to_add > 0:
            self.tokens = min(self.capacity, tokens_to_add + self.tokens)
            self.last_refill_time = now

    def allow_request(self, tokens_required: int = 1) -> bool:

        with self.lock:
            self.refill()

            if self.tokens >= tokens_required:
                self.tokens -= tokens_required
                return True
            return False


def worker(user_id: int, limiter: TokenBucketRateLimiter):
    for i in range(5):
        allowed = limiter.allow_request()

        if allowed:
            print(f"User {user_id} request {i} allowed")
        else:
            print(f"User {user_id} request {i} rejected")

        time.sleep(0.2)


def test_allows_up_to_capacity_then_rejects():
    from unittest.mock import patch

    with patch("time.monotonic", return_value=100.0):
        limiter = TokenBucketRateLimiter(capacity=3, refill_rate=1)

        assert limiter.allow_request() is True
        assert limiter.allow_request() is True
        assert limiter.allow_request() is True
        # bucket empty, no time elapsed -> rejected
        assert limiter.allow_request() is False


def test_refills_over_time():
    from unittest.mock import patch

    with patch("time.monotonic") as clock:
        clock.return_value = 100.0
        limiter = TokenBucketRateLimiter(capacity=2, refill_rate=1)

        assert limiter.allow_request() is True
        assert limiter.allow_request() is True
        assert limiter.allow_request() is False

        # 1 second later -> 1 token refilled (refill_rate=1)
        clock.return_value = 101.0
        assert limiter.allow_request() is True
        assert limiter.allow_request() is False


def test_refill_caps_at_capacity():
    from unittest.mock import patch

    with patch("time.monotonic") as clock:
        clock.return_value = 100.0
        limiter = TokenBucketRateLimiter(capacity=2, refill_rate=10)

        # long idle period would over-refill, but tokens cap at capacity
        clock.return_value = 200.0
        assert limiter.allow_request() is True
        assert limiter.allow_request() is True
        assert limiter.allow_request() is False


if __name__ == "__main__":
    # bucket size = 5
    # refill = 2 tokens per second
    limiter = TokenBucketRateLimiter(capacity=5, refill_rate=2)

    with ThreadPoolExecutor(max_workers=4) as executor:
        for user_id in range(4):
            executor.submit(worker, user_id, limiter)