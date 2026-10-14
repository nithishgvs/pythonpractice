import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.min_heap = []
        self.k = k
        for n in nums:
            self.heap_condition(n)

    def heap_condition(self, n):
        heapq.heappush(self.min_heap, n)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        self.heap_condition(val)
        return self.min_heap[0]


def test():
    s = KthLargest(3, [4, 5, 8, 2])
    print(s.add(3))
    print(s.add(5))
    print(s.add(10))
    print(s.add(9))
    print(s.add(4))
