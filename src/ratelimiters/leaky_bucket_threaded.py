import threading
import time
from queue import Queue


class LeakyBucketThreaded:
    def __init__(self, capacity, leak_rate):
        self.leak_rate = leak_rate
        self.bucket = Queue(maxsize=capacity)
        worker = threading.Thread(target=self.leak, daemon=True)
        worker.start()

    def add_request(self, request):
        if self.bucket.full():
            print(f"Rejected | Bucket full")
        else:
            self.bucket.put(request)
            print(f"Added | {request}")

    def leak(self):
        while True:
            if not self.bucket.empty():
                req = self.bucket.get()
                print(f"Processing {req}")
                time.sleep(1 / self.leak_rate)


if __name__ == "__main__":
    bucket = LeakyBucketThreaded(capacity=5, leak_rate=2)
    for i in range(10):
        bucket.add_request(f"Req-{i}")
        time.sleep(0.2)
