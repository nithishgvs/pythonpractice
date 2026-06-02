import heapq
from typing import List

import pytest


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)


@pytest.fixture
def solution():
    return Solution()


def test_first(solution):
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
