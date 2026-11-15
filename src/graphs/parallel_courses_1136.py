from collections import defaultdict, deque


class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        adjacency_list = defaultdict(list)
        indegree = [0] * n

        for previous_course, next_course in relations:
            adjacency_list[previous_course].append(next_course)
            indegree[next_course - 1] += 1
        semesters = 0
        completed_courses = 0

        queue = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            size = len(queue)
            semesters += 1
            for _ in range(size):
                node = queue.popleft()
                completed_courses += 1
                adjacents = adjacency_list.get(node + 1, [])
                for a in adjacents:
                    indegree[a - 1] -= 1
                    if indegree[a - 1] == 0:
                        queue.append(a - 1)

        return semesters if completed_courses == n else -1


def test():
    s = Solution()
    print(s.minimumSemesters(3, [[1, 2], [2, 3], [3, 1]]))
