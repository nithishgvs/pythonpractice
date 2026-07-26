class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s) + 1
        n = len(t) + 1

        if m > n:
            return False

        dp = [[0] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return m - 1 == dp[m - 1][n - 1]


def test1():
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
