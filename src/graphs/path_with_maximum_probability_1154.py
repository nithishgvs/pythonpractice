import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        graph = defaultdict(list)

        for i, (src, dst) in enumerate(edges):
            graph[src].append((-succProb[i], dst))
            graph[dst].append((-succProb[i], src))

        max_heap = [(-1.0, start_node)]

        visited = set()

        while max_heap:

            prob, node = heapq.heappop(max_heap)

            if node in visited:
                continue

            if node == end_node:
                return -prob

            visited.add(node)

            for next_prob, neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(max_heap, (-(prob * next_prob), neighbor))

        return 0.0


def test1():
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start_node = 0
    end_node = 2
    sol = Solution()
    result = sol.maxProbability(n, edges, succProb, start_node, end_node)
    print(result)  # Expected: 0.25
    assert result == 0.25


def test_no_path():
    n = 3
    edges = [[0, 1]]
    succProb = [0.5]
    start_node = 0
    end_node = 2
    sol = Solution()
    result = sol.maxProbability(n, edges, succProb, start_node, end_node)
    assert result == 0.0


def test_start_is_end():
    sol = Solution()

    assert sol.maxProbability(3, [[0, 1]], [0.5], 2, 2) == 1.0
