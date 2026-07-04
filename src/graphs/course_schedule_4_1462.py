from collections import defaultdict, deque
from typing import List


class Solution:
    def checkIfPrerequisite(
            self,
            numCourses: int,
            prerequisites: List[List[int]],
            queries: List[List[int]],
    ) -> List[bool]:
        result = []

        indegree = [0] * numCourses

        graph = defaultdict(list)

        for src, dst in prerequisites:
            graph[src].append(dst)
            indegree[dst] += 1

        queue = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)

        cache = [[False] * numCourses for _ in range(numCourses)]

        while queue:

            node = queue.popleft()

            for dst in graph[node]:
                cache[node][dst] = True
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    queue.append(dst)

                for i in range(numCourses):
                    if cache[i][node]:
                        cache[i][dst] = True

        for src, dst in queries:
            result.append(cache[src][dst])

        return result


def test_1():
    sol = Solution()
    numCourses = 4

    prerequisites = [
        [0, 1],
        [1, 2],
        [2, 3]
    ]

    queries = [
        [0, 3],  # True: 0 -> 1 -> 2 -> 3
    ]

    expected = [
        True
    ]

    assert sol.checkIfPrerequisite(numCourses, prerequisites=prerequisites, queries=queries) == expected
