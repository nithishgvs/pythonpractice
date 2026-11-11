from collections import deque


class HitCounter:

    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()

        return len(self.hits)


def test():
    hitCounter = HitCounter()
    hitCounter.hit(1)
    hitCounter.hit(2)
    hitCounter.hit(3)
    hitCounter.getHits(4)
    hitCounter.hit(300)
    hitCounter.getHits(300)
    hitCounter.getHits(301)
