import collections
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency_map = defaultdict(list)

        for sub_list in times:
            from_node = sub_list[0]
            to_node = sub_list[1]
            time = sub_list[2]
            adjacency_map[from_node].append((to_node, time))

        heap = [(0, k)]

        shortest = {}

        while heap:
            time, node = heapq.heappop(heap)

            if node in shortest:
                continue

            shortest[node] = time

            for to_node, new_time in adjacency_map[node]:
                heapq.heappush(heap, (time + new_time, to_node))

            if len(shortest) == n:
                return max(shortest.values())

        return -1


def test_1():
    solution = Solution()
    print(solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    print(solution.networkDelayTime([[1, 2, 1]], 2, 2))
