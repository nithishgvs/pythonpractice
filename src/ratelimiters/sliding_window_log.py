import queue
import threading
import time


class SlingWindowRateLimiter:
    def __init__(self, limit, window_size):
        self.limit = limit  # max no of requests allowed
        self.window_size = window_size  # time window in seconds
        self.lock = threading.Lock()
        self.timestamps = queue.Queue()  # store the time stamps

    def allow_request(self):
        now = time.time()
        with self.lock:
            # remove expired requests
            while self.timestamps and self.timestamps[0] <= now - self.window_size:
                self.timestamps.popleft()
            if len(self.timestamps) <= self.limit:
                self.timestamps.append(now)
                return True
            return False
