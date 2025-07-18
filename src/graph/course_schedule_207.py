from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build the graph and indegree map
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        # Start with courses having no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses


