# https://www.youtube.com/watch?v=-fx6aDxcWyg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=25
def lowest_common_subsequence(word1, word2):
    rows = len(word1) + 1
    cols = len(word2) + 1

    t = [[0] * cols for _ in range(rows)]

    for r in range(1, rows):
        for c in range(1, cols):

            if word1[r - 1] == word2[c - 1]:
                t[r][c] = 1 + t[r - 1][c - 1]
            else:
                t[r][c] = max(t[r - 1][c], t[r][c - 1])
    return t[rows - 1][cols - 1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lcs = lowest_common_subsequence(word1, word2)
        return len(word1) - lcs + len(word2) - lcs


def test():
    s = Solution()
    print(s.minDistance("heap", "pea"))
