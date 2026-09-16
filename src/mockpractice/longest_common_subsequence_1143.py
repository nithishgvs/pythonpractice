class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def solve(m: int, n: int) -> int:
            if n == 0 or m == 0:
                return 0

            if (m, n) in dp:
                return dp[(m, n)]

            result = 0

            if text1[m - 1] == text2[n - 1]:
                result = 1 + solve(m - 1, n - 1)

            else:
                result = max(solve(m - 1, n), solve(m, n - 1))

            dp[(m, n)] = result

            return result

        return solve(len(text1), len(text2))
