from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = 0
        max_consecutive_ones = 0

        for i, num in enumerate(nums):
            if num != 1:
                start = i + 1

            max_consecutive_ones = max(i - start + 1, max_consecutive_ones)

        return max_consecutive_ones


def test_max():
    solution = Solution();
    print(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
