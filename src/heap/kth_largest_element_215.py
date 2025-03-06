import heapq
from typing import List


class KthLargestElement:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for n in nums:
            heapq.heappush(min_heap, n)

            if (len(min_heap) > k):
                heapq.heappop(min_heap)

        return heapq.heappop(min_heap)


def test_kth_largest():
    object = KthLargestElement();
    print(object.find_kth_largest([3, 2, 1, 5, 6, 4], 2))
