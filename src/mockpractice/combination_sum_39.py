from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []
        curr_list: List[int]=[]

        def backtrack(start: int, remaining: int):

            if remaining == 0:
                result.append(curr_list.copy())
                return

            for i in range(start, len(candidates)):
                if candidates[i] <= remaining:
                    curr_list.append(candidates[i])
                    backtrack(i, remaining - candidates[i])
                    curr_list.pop()

        backtrack(0, target)

        return result


def test():
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
