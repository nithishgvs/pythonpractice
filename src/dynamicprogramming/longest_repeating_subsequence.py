class Solution:
    def longestRepeatingSubseq(self, s: str) -> int:
        """Length of longest subsequence that appears twice with no shared indices.

        Equivalent to LCS(s, s) where a match is only allowed when the two
        positions differ (r != c). Example: "aaaa" -> 3, "AABEBCDD" -> 3.
        """
        n = len(s)
        t = [[0] * (n + 1) for _ in range(n + 1)]

        for r in range(1, n + 1):
            for c in range(1, n + 1):
                if s[r - 1] == s[c - 1] and r != c:
                    t[r][c] = 1 + t[r - 1][c - 1]
                else:
                    t[r][c] = max(t[r - 1][c], t[r][c - 1])
        return t[n][n]


def test1():
    s = Solution()
    assert s.longestRepeatingSubseq("axxzxy") == 2
    assert s.longestRepeatingSubseq("aab") == 1
    assert s.longestRepeatingSubseq("aaaa") == 3
    assert s.longestRepeatingSubseq("AABEBCDD") == 3
    assert s.longestRepeatingSubseq("aabb") == 2
    assert s.longestRepeatingSubseq("") == 0
    assert s.longestRepeatingSubseq("a") == 0
    assert s.longestRepeatingSubseq("aa") == 1
    print("all tests passed")
