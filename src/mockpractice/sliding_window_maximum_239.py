from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        queue = deque()

        for i, value in enumerate(nums):
            # we only add indices
            while queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] <= value:
                queue.pop()
            queue.append(i)

            if i >= k - 1:
                result.append(nums[queue[0]])
        return result


def test():
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
