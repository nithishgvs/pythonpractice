def is_palindrome(s, i, j):
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


class Solution:
    def minCut(self, s: str) -> int:

        dp = {}

        def solve(s: str, i: int, j: int) -> int:

            if (i, j) in dp:
                return dp[(i, j)]

            if i >= j or is_palindrome(s, i, j):
                dp[(i, j)] = 0
                return 0

            min_cut = float("inf")
            for k in range(i, j):
                if (i, k) not in dp:
                    left = solve(s, i, k)
                    dp[(i, k)] = left
                else:
                    left = dp[(i, k)]

                if (k + 1, j) not in dp:
                    right = solve(s, k + 1, j)
                    dp[(k + 1, j)] = right
                else:
                    right = dp[(k + 1, j)]
                temp_min = 1 + left + right
                min_cut = min(temp_min, min_cut)
                dp[(i, j)] = min_cut
            return min_cut

        return solve(s, 0, len(s) - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.minCut("coder"))
