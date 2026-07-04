import threading
import time


class FixedWindowRateLimiter:
    def __init__(self, limit, window_size):
        self.limit = limit
        self.window_size = window_size
        self.counter = 0
        self.lock = threading.Lock()
        self.window_start = time.time()

    def allow_request(self):
        with self.lock:
            now = time.time()

        if now - self.window_start >= self.window_size:
            self.window_start = 0
            self.counter = 0

        if self.counter < self.limit:
            self.counter += 1
            return True
        return False
