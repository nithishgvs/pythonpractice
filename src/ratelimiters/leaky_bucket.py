import time


class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.water = 0  # current no of requests allowed in the bucket
        self.last_check = time.time()

    def allow_request(self):
        now = time.time()
        elapsed = now - self.last_check
        leaked = elapsed * self.leak_rate

        self.water = max(0, self.water - leaked)

        self.last_check = now

        if self.water + 1 <= self.capacity:
            self.water += 1
            print(f"Accepted | Bucket level: {self.water:.2f}")
            return True
        else:
            print(f"Rejected | Bucket full")
            return False


def test_allows_requests_until_bucket_is_full():
    from unittest.mock import patch

    bucket = LeakyBucket(capacity=2, leak_rate=1)

    with patch("time.time", return_value=bucket.last_check):
        assert bucket.allow_request() is True
        assert bucket.allow_request() is True
        assert bucket.allow_request() is False


def test_leaks_water_over_time():
    from unittest.mock import patch

    bucket = LeakyBucket(capacity=2, leak_rate=1)

    with patch("time.time", return_value=bucket.last_check):
        assert bucket.allow_request() is True
        assert bucket.allow_request() is True

    with patch("time.time", return_value=bucket.last_check + 1):
        assert bucket.allow_request() is True


if __name__ == "__main__":
    bucket = LeakyBucket(capacity=5, leak_rate=1)
    for i in range(100):
        bucket.allow_request()
        time.sleep(0.2)
