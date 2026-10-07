import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Keep the k largest values seen so far in a min-heap.
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # The smallest value among the k largest is the kth largest overall.
        return min_heap[0]


def test():
    s = Solution()
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 1) == 6
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 6) == 1
