class Solution:
    def minInsertions(self, s: str) -> int:

        rows = len(s) + 1
        rev = s[::-1]

        t = [[0] * rows for _ in range(rows)]

        for i in range(1, rows):
            for j in range(1, rows):
                if s[i - 1] == rev[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])
        return len(s) - t[rows - 1][rows - 1]
def test1():
    s = Solution()
    print(s.minInsertions("mbadm"))