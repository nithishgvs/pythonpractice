import heapq
from typing import List


class Solution:

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # queue to order tasks by the enqueue time
        processing_queue = []
        for i in range(0, len(tasks)):
            heapq.heappush(processing_queue, (tasks[i][0], (i, tasks[i][0], tasks[i][1])))

        result = []
        current_time = 1

        available_tasks_to_process = []

        while processing_queue or available_tasks_to_process:

            while processing_queue and processing_queue[0][1][1] <= current_time:
                task = heapq.heappop(processing_queue)
                heapq.heappush(available_tasks_to_process, (task[1][2], task[1][0], task[1]))

            if available_tasks_to_process:
                available_task = heapq.heappop(available_tasks_to_process)
                result.append(available_task[2][0])
                current_time += available_task[2][2]
            else:
                current_time = processing_queue[0][1][1]

        return result


def test_cpu():
    object = Solution()
    print(object.getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))
