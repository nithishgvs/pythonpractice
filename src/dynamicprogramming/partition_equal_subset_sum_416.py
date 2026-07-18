from typing import List


class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        # Bottom-up tabulation: t[r][c] = can the first r elements make sum c.
        # Table has (n+1) rows and (need_sum+1) columns, each cell filled in O(1).
        # Time: O(n * need_sum), i.e. O(n * total). Space: O(n * need_sum) for the table.
        total = sum(nums)

        if total % 2 != 0:
            return False

        need_sum = total // 2

        rows = len(nums) + 1
        cols = need_sum + 1

        t = [[False] * cols for _ in range(rows)]

        for r in range(rows):
            t[r][0] = True

        for r in range(1, rows):
            for c in range(1, cols):
                if nums[r - 1] <= c:
                    t[r][c] = t[r - 1][c] or t[r - 1][c - nums[r - 1]]
                else:
                    t[r][c] = t[r - 1][c]

        return t[rows-1][cols-1]

    def canPartition1(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        total_needed = total // 2

        # Each recursive state is (curr_index, curr_sum).
        # curr_index has n possible values (one for each position in nums).
        # curr_sum has total_needed possible values (0 through total_needed).
        # Therefore, there are at most n * total_needed unique states.
        # Memoization calculates each state only once: time O(n * total_needed).
        # Since total_needed is total / 2, this is also O(n * total).
        # dp stores those states: space O(n * total_needed), plus O(n) recursion.
        dp = {}

        def helper(curr_index, curr_sum) -> bool:
            if total_needed == curr_sum:
                return True

            if curr_index == len(nums):
                return False

            if (curr_index, curr_sum) in dp:
                return dp[(curr_index, curr_sum)]

            if nums[curr_index] + curr_sum <= total_needed:
                can_use = helper(curr_index + 1, nums[curr_index] + curr_sum)
                cant_use = helper(curr_index + 1, curr_sum)
                result = can_use or cant_use
            else:
                result = helper(curr_index + 1, curr_sum)

            dp[(curr_index, curr_sum)] = result
            return result

        return helper(0, 0)


def test():
    sol = Solution()
    print(sol.canPartition([1, 5, 5, 11]))
