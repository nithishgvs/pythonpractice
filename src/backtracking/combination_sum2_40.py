from typing import List


class Solution:
    # Let n = len(candidates).
    # Time:  O(2^n) - each element is either chosen or skipped (the duplicate
    #        skip prunes branches but the worst case is still 2^n subsets),
    #        plus O(n) to copy each valid combination, and O(n log n) to sort.
    # Space: O(n) for the recursion stack and curr_list (excluding the output).
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []
        candidates.sort()

        def backtrack(index: int, curr_sum: int, curr_list: List[int]):

            if curr_sum == target:
                result.append(curr_list.copy())
                return

            if curr_sum > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                curr_sum += candidates[i]
                curr_list.append(candidates[i])
                backtrack(i + 1, curr_sum, curr_list)
                curr_sum -= candidates[i]
                curr_list.pop()

        backtrack(0, 0, [])
        return result


def test_1():
    solution = Solution()
    result = solution.combinationSum2([2, 5, 2, 1, 2], 5)

    assert sorted(result) == sorted([[1, 2, 2], [5]])


def test_2():
    solution = Solution()
    result = solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)

    assert sorted(result) == sorted(
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    )
