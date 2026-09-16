from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []

        def solve(start: int):

            if start == len(nums):
                result.append(nums.copy())
                return

            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                solve(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        solve(0)
        return result


def test():
    s = Solution()
    print(s.permute([1, 2]))
