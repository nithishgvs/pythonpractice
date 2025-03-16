import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = Counter(tasks)
        max_heap = [(-freq, task) for task, freq in freq_map.items()]
        heapq.heapify(max_heap)

        time = 0
        cooldown_queue = deque()

        while max_heap or cooldown_queue:
            time += 1

            if max_heap:
                freq, task = heapq.heappop(max_heap)

                if abs(freq) > 1:
                    cooldown_queue.append((time + n, task, abs(freq) - 1))

            if cooldown_queue and cooldown_queue[0][0] == time:
                _, task, freq = cooldown_queue.popleft()
                heapq.heappush(max_heap, (-freq, task))
        return time


def test_least():
    solution = Solution()
    print(solution.leastInterval(["A", "C", "A", "B", "D", "B"], 1))
