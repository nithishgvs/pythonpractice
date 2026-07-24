def lcs_rec_mem(text1, text2, m, n, count, dp):
    if m == 0 or n == 0:
        return count

    key = (m, n, count)
    if key in dp:
        return dp[key]

    current_count = count
    if text1[m - 1] == text2[n - 1]:
        current_count = lcs_rec_mem(text1, text2, m - 1, n - 1, count + 1, dp)
    skip_from_first = lcs_rec_mem(text1, text2, m - 1, n, 0, dp)
    skip_from_second = lcs_rec_mem(text1, text2, m, n - 1, 0, dp)

    dp[key] = max(current_count, skip_from_first, skip_from_second)
    return dp[key]


class Solution:

    def longestCommonSubstring1(self, text1: str, text2: str) -> int:
        # dp[row][col] is the length of the common substring ending at
        # text1[row - 1] and text2[col - 1].
        rows = len(text1) + 1
        cols = len(text2) + 1
        dp = [[0] * cols for _ in range(rows)]
        maximum_length = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                    maximum_length = max(maximum_length, dp[row][col])
                # A mismatch leaves dp[row][col] as 0, ending this substring.

        return maximum_length

    def longestCommonSubstring(self, text1: str, text2: str) -> int:
        dp = {}
        return lcs_rec_mem(text1, text2, len(text1), len(text2), 0, dp)


def test1():
    solution = Solution()
    print(solution.longestCommonSubstring("abcd", "acd"))
