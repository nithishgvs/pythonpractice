from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []

        indegree = [0] * numCourses
        graph = defaultdict(list)

        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            node = queue.popleft()
            result.append(node)
            for value in graph[node]:
                indegree[value] -= 1
                if indegree[value] == 0:
                    queue.append(value)

        return result if len(result) == numCourses else []


def test_course():
    object = Solution()
    print(object.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
