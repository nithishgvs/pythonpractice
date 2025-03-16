import heapq
from typing import List


class KthLargest:
    min_heap = []
    total = 0

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.total = k
        for num in nums:
            heapq.heappush(self.min_heap, num)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.total:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


def test_kthlargest():
    object = KthLargest(3, [4, 5, 8, 2])
    print(object.add(3))
    print(object.add(5))
    print(object.add(10))
    print(object.add(9))
    print(object.add(4))
