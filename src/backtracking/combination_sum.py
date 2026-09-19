class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []
        n = len(candidates)

        def solve(start_index: int, curr_sum: int, curr_list: list[int]):

            if curr_sum > target:
                return

            if curr_sum == target:
                result.append(curr_list.copy())
                return

            for i in range(start_index, n):
                curr_list.append(candidates[i])
                solve(i, curr_sum + candidates[i], curr_list)
                curr_list.pop()

        solve(0, 0, [])
        return result


def test():
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
