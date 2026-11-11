import heapq
import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        result = []
        for p0, p1 in points:
            result.append((p0, p1, math.pow(p0, 2) + math.pow(p1, 2)))
        return [[item[0], item[1]] for item in heapq.nsmallest(k, result, key=lambda s: s[2])]


def test():
    s = Solution()
    print(s.kClosest([[2, 2], [2, 2], [3, 3], [2, -2], [1, 1]], 4))
