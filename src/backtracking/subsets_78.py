from typing import List


class Solution:
    # Time:  O(n * 2^n) - there are 2^n subsets, and copying each into the
    #        result takes up to O(n).
    # Space: O(n) for the recursion stack and curr_list (excluding the output).
    #        Including the output it is O(n * 2^n).
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []

        def dfs(index: int, curr_list: List[int]) -> None:
            if index >= len(nums):
                result.append(curr_list.copy())
                return

            curr_list.append(nums[index])
            dfs(index + 1, curr_list)
            curr_list.pop()
            dfs(index + 1, curr_list)

        dfs(0, [])
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
