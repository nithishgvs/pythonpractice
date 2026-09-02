from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(current_list: List[int], index: int, curr_sum: int):
            if curr_sum == target:
                result.append(current_list.copy())
                return
            if curr_sum > target or index >= len(candidates):
                return

            for i in range(index, len(candidates)):
                current_list.append(candidates[i])
                curr_sum += candidates[i]
                backtrack(current_list, i, curr_sum)
                curr_sum -= candidates[i]
                current_list.pop()
        backtrack([], 0, 0)
        return result


def test():
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
