from typing import List

"""
This is a version of ->Count the number of subset with a given difference
You are going to divide the array into 2 subsets with sum diff equal to target

s1-s2=target and s1+s2=total(sum of nums) which we do as range
add both 2(s1)=target+total(sum of nums)-> s1 = (target+total(sum of nums))/2
we need to check if we can find the subsets which make up to this value
"""


class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)
        if abs(target) > total or (target + total) % 2 != 0:
            return 0
        subset_sum = (target + total) // 2
        rows = len(nums) + 1
        cols = subset_sum + 1

        t = [[0] * cols for _ in range(rows)]
        t[0][0] = 1

        for row in range(1, rows):
            num = nums[row - 1]
            for col in range(cols):

                if num <= col:
                    # can take or cant take
                    t[row][col] = t[row - 1][col] + t[row - 1][col - num]
                else:
                    t[row][col] = t[row - 1][col]
        return t[rows - 1][cols - 1]

    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (target + total) % 2 != 0:
            return 0
        subset_sum = (target + total) // 2
        n = len(nums)
        dp = {}

        def find_subset_sum(n, subset_sum):

            if n == 0:
                return 1 if subset_sum == 0 else 0

            if (n, subset_sum) in dp:
                return dp[(n, subset_sum)]

            if nums[n - 1] <= subset_sum:
                # with and without check
                result = find_subset_sum(n - 1, subset_sum) + find_subset_sum(n - 1, subset_sum - nums[n - 1])
            else:
                result = find_subset_sum(n - 1, subset_sum)

            dp[(n, subset_sum)] = result
            return result

        return find_subset_sum(n, subset_sum)


def test1():
    sol = Solution()
    print(sol.findTargetSumWays([1, 1, 1, 1, 1], 3))
