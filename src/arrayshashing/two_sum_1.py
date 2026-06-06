from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], idx]
            seen[num] = idx

        return []


def test_1():
    nums = [2, 7, 11, 15]
    obj = Solution()
    assert obj.twoSum(nums, 9) == [0, 1]
