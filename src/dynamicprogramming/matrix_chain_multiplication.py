"""
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications. The dimensions of the matrices are given in an array arr[] of size n (such that n = number of matrices + 1) where the ith matrix has the dimensions (arr[i-1] x arr[i]).

Examples:

Input: arr[] = [2, 1, 3, 4]
Output: 20
Explanation: There are 3 matrices of dimensions 2×1, 1×3, and 3×4, Let the input 3 matrices be M1, M2, and M3. There are two ways to multiply ((M1 x M2) x M3) and (M1 x (M2 x M3)), Please note that the result of M1 x M2 is a 2 x 3 matrix and result of (M2 x M3) is a 1 x 4 matrix.
((M1 x M2) x M3)  requires (2 x 1 x 3)  + (0) +  (2 x 3 x 4) = 30
(M1 x (M2 x M3))  requires (0)  + (1 x 3 x 4) +  (2 x 1 x 4) = 20
The minimum of these two is 20.
Input: arr[] = [1, 2, 3, 4, 3]
Output: 30
"""


class Solution:
    def matrix_chain_multiplication(self, nums) -> int:
        dp = {}

        def solve(i, j):
            if i >= j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            best = float("inf")
            for k in range(i, j):
                cost = solve(i, k) + solve(k + 1, j) + nums[i - 1] * nums[k] * nums[j]
                best = min(best, cost)

            dp[(i, j)] = best   # cache the TRUE minimum for this (i, j) range
            return best

        return solve(1, len(nums) - 1)


if __name__ == "__main__":
    arr = [2, 1, 3, 4]
    res = Solution()
    print(res.matrix_chain_multiplication(arr))  # 20