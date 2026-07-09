from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(nums, start):
            if start == len(nums):
                result.append(nums.copy())
                return

            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtracking(nums, start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtracking(nums, 0)
        return result


def test1():
    sol = Solution()
    print(sol.permute([1, 2, 3]))
