"""
https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
Given an array of positive integers arr[] and a value sum, determine if there is a subset of arr[] with sum equal to given sum.
Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 9
Output: true
Explanation: Here there exists a subset with target sum = 9, 4+3+2 = 9.
"""


class Solution:
    def isSubsetSum(self, arr, sum):
        # matrix we take sum+1 and n+1 so we provide base condition here
        rows = len(arr) + 1
        cols = sum + 1
        t = [[False] * cols for _ in range(rows)]

        for row in range(rows):
            t[row][0] = True

        for col in range(1, cols):
            t[0][col] = False

        for r in range(1, rows):
            for c in range(1, cols):

                if arr[r - 1] <= c:
                    # include
                    can_take = t[r - 1][c - arr[r - 1]]
                    # cant include
                    cant_take = t[r - 1][c]
                    t[r][c] = can_take or cant_take
                else:
                    # cant include
                    t[r][c] = t[r - 1][c]

        return t[rows - 1][cols - 1]


def test():
    s = Solution()
    print(s.isSubsetSum([2, 2, 4], 4))
