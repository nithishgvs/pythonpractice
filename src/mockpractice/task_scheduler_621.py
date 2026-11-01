import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_map = Counter(tasks)
        max_heap = []
        for k, v in task_map.items():
            heapq.heappush(max_heap, (-v, k))
        result = []
        queue = deque()
        while max_heap:
            for _ in range(n + 1):
                if len(max_heap) > 0:
                    v, k = heapq.heappop(max_heap)
                    if abs(v) > 1:
                        queue.append((v + 1, k))
                    result.append(k)
                elif len(queue) > 0:
                    result.append("idle")
            while queue:
                v, k = queue.popleft()
                heapq.heappush(max_heap, (v, k))
        return len(result)


if __name__ == "__main__":
    s = Solution()
    print(s.leastInterval(["A","A","A","B","B","B"], 2))
