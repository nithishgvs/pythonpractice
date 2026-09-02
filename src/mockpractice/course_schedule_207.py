from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        total_finished = 0

        indegree = [0] * numCourses

        hash_map = defaultdict(list)

        for dest, src in prerequisites:
            hash_map[src].append(dest)
            indegree[dest] += 1

        queue = deque()

        for index, indeg in enumerate(indegree):
            if indeg == 0:
                queue.append(index)

        while queue:
            node = queue.popleft()
            total_finished += 1

            for adj in hash_map.get(node,[]):
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)

        return total_finished == numCourses


def test():
    s = Solution()
    print(s.canFinish(2, [[1, 0],[0, 1]]))
