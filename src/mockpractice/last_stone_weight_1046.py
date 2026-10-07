import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            if first != second:
                heapq.heappush(max_heap, -(first - second))

        return -max_heap[0] if len(max_heap) == 1 else 0


def test():
    s = Solution()
    print(s.lastStoneWeight([2, 2]))
