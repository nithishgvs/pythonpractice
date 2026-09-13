from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result: List[int] = []

        indegree = [0] * numCourses

        adjacency_map: dict[int, List[int]] = {}

        for to_node, from_node in prerequisites:
            adjacency_map.setdefault(from_node, []).append(to_node)
            indegree[to_node] += 1

        queue = deque()

        for idx, indeg in enumerate(indegree):
            if indeg == 0:
                queue.append(idx)

        while queue:
            node = queue.popleft()
            result.append(node)

            adjacent_nodes = adjacency_map.get(node, [])

            for adj in adjacent_nodes:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)

        return [] if len(result) != numCourses else result


def test():
    s = Solution()
    print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
