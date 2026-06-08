from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        completed_courses = 0

        indegree = [0] * numCourses

        graph = defaultdict(list)

        for pre in prerequisites:
            from_course = pre[1]
            to_course = pre[0]
            indegree[to_course] += 1
            graph[from_course].append(to_course)

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            popped = queue.popleft()
            completed_courses += 1

            for child in graph[popped]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        return completed_courses == numCourses


def test1():
    prerequisites = [[1, 0], [0, 1]]
    solution = Solution()
    assert solution.canFinish(2, prerequisites) is False
    assert solution.canFinish(2, [[1, 0]]) is True
