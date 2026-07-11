# https://www.geeksforgeeks.org/dsa/find-maximum-number-possible-by-doing-at-most-k-swaps/
# Aditya verma video Back Tracking

class Solution:

    # Time: O(n * n!) - the else branch recurses on every i regardless of whether
    #   a swap happened, without spending k, so depth is bounded by n (not k) and
    #   most paths use 0 swaps and are never pruned by k. Branching factor n at
    #   depth 0, n-1 at depth 1, ... gives a Theta(n!) call tree (verified: call
    #   counts for k=n match f(m)=1+m*f(m-1)), times O(n) work per call to find
    #   the max remaining digit. k barely reduces this since it rarely gets spent.
    # Space: O(n) - the digits list/max_number snapshot plus O(n) recursion stack.
    def findMax(self, s, k):
        digits = list(s)
        max_number = digits[:]

        def backtracking(start, s, k):
            nonlocal max_number
            # base condition
            if k == 0 or start == len(s) - 1:
                return

            # Gotta find max from start+1 to end
            maximum = s[start]
            for i in range(start + 1, len(s)):
                maximum = max(s[i], maximum)

            for i in range(start + 1, len(s)):

                if s[i] > s[start] and s[i] == maximum:
                    # swap logic
                    s[i], s[start] = s[start], s[i]
                    max_number = max(max_number, s[:])
                    backtracking(start + 1, s, k - 1)
                    s[start], s[i] = s[i], s[start]
                else:
                    backtracking(start + 1, s, k)

        backtracking(0, digits, k)
        return "".join(max_number)


def test_1():
    sol = Solution()
    print(sol.findMax("1234", 2))
