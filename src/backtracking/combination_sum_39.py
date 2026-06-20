from typing import List


class Solution:
    # Let n = len(candidates) and t = target / min(candidates) be the max
    # recursion depth (longest combination).
    # Time:  O(n^t) - branching up to n choices at each of t levels, plus
    #        O(t) to copy each valid combination into the result.
    # Space: O(t) for the recursion stack and curr_list (excluding the output).
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index: int, curr_sum: int, curr_list: List[int]):

            if curr_sum == target:
                result.append(curr_list.copy())
                return

            if curr_sum > target:
                return

            for i in range(index, len(candidates)):
                curr_sum += candidates[i]
                curr_list.append(candidates[i])
                backtrack(i, curr_sum, curr_list)
                curr_sum -= candidates[i]
                curr_list.pop()

        backtrack(0, 0, [])

        return result


def test_1():
    solution = Solution()
    result = solution.combinationSum([2, 3, 6, 7], 7)

    assert sorted(result) == sorted([[2, 2, 3], [7]])


def test_2():
    solution = Solution()
    result = solution.combinationSum([2, 3, 5], 8)

    assert sorted(result) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])


def test_3():
    solution = Solution()
    result = solution.combinationSum([2], 1)

    assert result == []
