class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):

                if c == 0:
                    dp[r][c] = 1
                    continue
                else:
                    dp[r][c] = dp[r][c - 1] + (dp[r - 1][c] if r - 1 > -1 else 0)

        return dp[m - 1][n - 1]


def test():
    s = Solution()
    print(s.uniquePaths(3, 7))
