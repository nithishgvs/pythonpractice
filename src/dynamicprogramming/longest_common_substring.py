class Solution:

    def longestCommonSubstring(self, text1: str, text2: str) -> int:
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


def test1():
    solution = Solution()
    print(solution.longestCommonSubstring("abcd", "acd"))
