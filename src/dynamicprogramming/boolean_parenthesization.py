"""
You are given a boolean expression s containing
    'T' ---> true
    'F' ---> false
and following operators between symbols
   &   ---> boolean AND
    |   ---> boolean OR
   ^   ---> boolean XOR
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

Note: The answer is guaranteed to fit within a 32-bit integer.
"""


class Solution:
    def countWays(self, s):
        # Time: O(n^3) — O(n^2) subexpressions, each trying O(n) operators.
        # Space: O(n^2) for memoization, plus O(n) recursion depth.
        memo = {}

        def solve(i, j):
            """Return (ways_to_true, ways_to_false) for s[i:j + 1]."""
            if i == j:
                return (1, 0) if s[i] == "T" else (0, 1)

            if (i, j) in memo:
                return memo[(i, j)]

            true_ways = false_ways = 0
            for k in range(i + 1, j, 2):
                left_true, left_false = solve(i, k - 1)
                right_true, right_false = solve(k + 1, j)

                if s[k] == "|":
                    true_ways += (
                            left_true * right_true
                            + left_true * right_false
                            + left_false * right_true
                    )
                    false_ways += left_false * right_false
                elif s[k] == "&":
                    true_ways += left_true * right_true
                    false_ways += (
                            left_true * right_false
                            + left_false * right_true
                            + left_false * right_false
                    )
                else:  # XOR
                    true_ways += left_true * right_false + left_false * right_true
                    false_ways += left_true * right_true + left_false * right_false

            memo[(i, j)] = (true_ways, false_ways)
            return memo[(i, j)]

        return solve(0, len(s) - 1)[0]


def test_1():
    sol = Solution()
    print(sol.countWays("T|T&F^T"))
