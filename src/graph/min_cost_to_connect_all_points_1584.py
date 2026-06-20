import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_cost = 0

        adjacency_map = defaultdict(list)

        n = len(points)
        # Each point is an index
        for i in range(n):
            for j in range(i + 1, n):
                # python unpacks list directly
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adjacency_map[i].append((distance, j))
                adjacency_map[j].append((distance, i))
        visited = set()

        min_heap = [(0, 0)]

        while min_heap:

            dist, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            visited.add(node)
            min_cost += dist

            for distance, neighbour in adjacency_map[node]:
                if neighbour not in visited:
                    heapq.heappush(min_heap, (distance, neighbour))

        return min_cost


def test_1():
    solution = Solution()
    assert solution.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18
    assert solution.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
