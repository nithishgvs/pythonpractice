import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for (x, y) in points:
            distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
            heapq.heappush(min_heap, (distance, x, y))

        return [[x, y] for _, x, y in heapq.nsmallest(k, min_heap)]


def test_kclosest():
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [0, 0]]
    k = 3
    solution = Solution()
    print(solution.kClosest(points, k))
