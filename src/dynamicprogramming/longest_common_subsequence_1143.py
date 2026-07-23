def lcs_recursion(text1: str, text2: str, n: int, m: int, dp: dict) -> int:
    if n == 0 or m == 0:
        return 0

    if (n, m) in dp:
        return dp[(n, m)]

    if text1[n - 1] == text2[m - 1]:
        result = 1 + lcs_recursion(text1, text2, n - 1, m - 1, dp)
    else:
        result = max(
            lcs_recursion(text1, text2, n - 1, m, dp),
            lcs_recursion(text1, text2, n, m - 1, dp),
        )
    dp[(n, m)] = result
    return result


class Solution:

    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        dp = {}
        return lcs_recursion(text1, text2, len(text1), len(text2), dp)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1
        cols = len(text2) + 1
        t = [[0] * cols for _ in range(rows)]

        for r in range(1, rows):
            for c in range(1, cols):
                if text1[r - 1] == text2[c - 1]:
                    t[r][c] = 1 + t[r - 1][c - 1]
                else:
                    t[r][c] = max(t[r - 1][c], t[r][c - 1])
        return t[rows - 1][cols - 1]


def test():
    s = Solution()
    print(s.longestCommonSubsequence("abcd", "abcx"))
