import heapq
from typing import List


class Solution:

    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        result, minheap = [], []

        for index, task in enumerate(tasks):
            task.append(index)

        # order tasks by the enqueue time
        tasks.sort(key=lambda t: t[0])
        i, time = 0, tasks[0][0]

        while i < len(tasks) or minheap:

            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minheap, [tasks[i][1], tasks[i][2]])
                i += 1

            if not minheap:
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(minheap)
                result.append(index)
                time += procTime

        return result


def test_cpu():
    object = Solution()
    print(object.getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))
