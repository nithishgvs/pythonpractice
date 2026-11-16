import heapq


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # Keep the lower half in a max heap and the upper half in a min heap.
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Keep the lower half the same size as the upper half, or one larger.
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return float(-self.max_heap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

def test():
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    obj.addNum(3)
    obj.addNum(4)
    obj.addNum(5)
    print(obj.findMedian())
