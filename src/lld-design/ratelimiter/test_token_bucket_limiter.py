import unittest
from unittest.mock import patch

import TokenBucketLimiter as token_bucket_module
from TokenBucketLimiter import TokenBucketLimiter


class TokenBucketLimiterTests(unittest.TestCase):
    def setUp(self):
        self.now = 1000.0
        self.time_patcher = patch.object(
            token_bucket_module.time, "time", side_effect=lambda: self.now
        )
        self.time_patcher.start()
        self.addCleanup(self.time_patcher.stop)

    def test_allows_requests_while_tokens_are_available(self):
        limiter = TokenBucketLimiter(capacity=2, refill_rate_per_second=1)

        first = limiter.allow("client")
        second = limiter.allow("client")

        self.assertTrue(first.is_allowed())
        self.assertEqual(first.get_remaining(), 1)
        self.assertIsNone(first.get_retry_after_ms())
        self.assertTrue(second.is_allowed())
        self.assertEqual(second.get_remaining(), 0)
        self.assertIsNone(second.get_retry_after_ms())

    def test_denies_when_empty_and_reports_time_to_next_token(self):
        limiter = TokenBucketLimiter(capacity=1, refill_rate_per_second=2)
        self.assertTrue(limiter.allow("client").is_allowed())

        denied = limiter.allow("client")

        self.assertFalse(denied.is_allowed())
        self.assertEqual(denied.get_remaining(), 0)
        self.assertEqual(denied.get_retry_after_ms(), 500)

    def test_refills_fractional_tokens_over_elapsed_time(self):
        limiter = TokenBucketLimiter(capacity=1, refill_rate_per_second=2)
        limiter.allow("client")
        self.now += 0.25

        denied = limiter.allow("client")

        self.assertFalse(denied.is_allowed())
        self.assertEqual(denied.get_retry_after_ms(), 250)

    def test_refill_never_exceeds_capacity(self):
        limiter = TokenBucketLimiter(capacity=1, refill_rate_per_second=1)
        self.now += 10

        result = limiter.allow("client")

        self.assertTrue(result.is_allowed())
        self.assertEqual(result.get_remaining(), 0)

    def test_client_buckets_are_independent(self):
        limiter = TokenBucketLimiter(capacity=1, refill_rate_per_second=1)

        self.assertTrue(limiter.allow("first").is_allowed())
        self.assertTrue(limiter.allow("second").is_allowed())
        self.assertFalse(limiter.allow("first").is_allowed())


if __name__ == "__main__":
    unittest.main()
