import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap=[]


        for point in points:
            distance=math.sqrt(math.pow(point[0],2)+math.pow(point[1],2))
            heapq.heappush(min_heap,(distance,point[0],point[1]))

        return  [[x, y] for distance, x, y in heapq.nsmallest(k, min_heap)]


def test_kclosest():
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [0, 0]]
    k = 3
    solution = Solution()
    print(solution.kClosest(points, k))
