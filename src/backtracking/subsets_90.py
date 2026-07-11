from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: List[List[int]] = []
        subsets: List[int] = []

        def backtrack(start):
            if start == len(nums):
                result.append(subsets.copy())
                return

            # subsets including nums[start]
            subsets.append(nums[start])
            backtrack(start + 1)
            subsets.pop()
            # subsets which dont include  nums[start] but also if nums[start]=nums[start+1]
            while start + 1 < len(nums) and nums[start] == nums[start + 1]:
                start += 1
            backtrack(start + 1)

        backtrack(0)
        return result


def test_1():
    solution = Solution()
    result = solution.subsetsWithDup([1, 2, 2])

    assert sorted(result) == sorted([[], [1], [2], [1, 2], [2, 2], [1, 2, 2]])


def test_2():
    solution = Solution()
    result = solution.subsetsWithDup([1, 2])

    assert sorted(result) == sorted([[], [1], [2], [1, 2]])
