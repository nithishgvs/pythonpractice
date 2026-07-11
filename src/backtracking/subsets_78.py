from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        subset: List[int] = []

        def backtracking(start):
            if start == len(nums):
                result.append(subset.copy())
                return
            # include the number
            subset.append(nums[start])
            backtracking(start + 1)
            # dont include the number
            subset.pop()
            backtracking(start + 1)

        backtracking(0)

        return result


def test_1():
    solution = Solution()
    result = solution.subsets([1, 2])

    assert sorted(result) == sorted([[], [1], [2], [1, 2]])


def test_2():
    solution = Solution()
    result = solution.subsets([1, 2, 3])

    assert sorted(result) == sorted(
        [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    )
