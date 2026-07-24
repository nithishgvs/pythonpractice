class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        rows = len(str1) + 1
        cols = len(str2) + 1

        t = [[0] * cols for _ in range(rows)]

        for r in range(1, rows):
            for c in range(1, cols):
                if str1[r - 1] == str2[c - 1]:
                    t[r][c] = 1 + t[r - 1][c - 1]
                else:
                    t[r][c] = max(t[r - 1][c], t[r][c - 1])
        i, j = rows - 1, cols - 1
        result = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            elif t[i - 1][j] > t[i][j - 1]:
                # here we got max not considering i so i has to be added
                result.append(str1[i - 1])
                i -= 1
            else:
                result.append(str2[j - 1])
                j -= 1

        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        while j > 0:
            result.append(str2[j - 1])
            j -= 1
        return "".join(reversed(result))

    def lcs(self, str1: str, str2: str) -> int:
        return self.lcs_recursion(str1, str2, len(str1), len(str2), {})

    def lcs_recursion(self, str1, str2, m, n, dp):
        if n == 0 or m == 0:
            return 0

        if (m, n) in dp:
            return dp[(m, n)]

        if str1[m - 1] == str2[n - 1]:
            # Both characters match.
            result = 1 + self.lcs_recursion(str1, str2, m - 1, n - 1, dp)
        else:
            result = max(
                self.lcs_recursion(str1, str2, m - 1, n, dp),
                self.lcs_recursion(str1, str2, m, n - 1, dp),
            )

        dp[(m, n)] = result
        return result


def test1():
    s = Solution()
    print(s.shortestCommonSupersequence("abac", "cab"))
