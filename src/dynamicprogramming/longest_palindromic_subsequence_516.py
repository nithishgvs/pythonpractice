class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # reverse string s and do lca of s and reverse(s)
        rev = s[::-1]
        rows = len(s) + 1
        cols = len(s) + 1
        t = [[0] * cols for _ in range(rows)]

        for r in range(1, rows):
            for c in range(1, cols):
                if s[r - 1] == rev[c - 1]:
                    t[r][c] = 1 + t[r - 1][c - 1]
                else:
                    t[r][c] = max(t[r - 1][c], t[r][c - 1])
        return t[rows - 1][cols - 1]


def test():
    s = Solution()
    print(s.longestPalindromeSubseq("abbd"))
