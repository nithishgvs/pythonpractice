class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # This substring-based version is O(n^5) time in the worst case:
        # O(n^3) memo states × O(n) split points × O(n) slicing/key creation.
        # Space is O(n^4) in the worst case because memo keys store substrings.
        # Using indices instead of slices/strings reduces this to O(n^4) time
        # and O(n^3) space.

        if len(s1) != len(s2):
            return False
        memo = {}

        def solve(s1: str, s2: str) -> bool:
            key = s1 + " " + s2
            if key in memo:
                return memo[key]
            # Base conditions
            if s1 == s2:
                memo[key] = True
                return True
            if len(s1) <= 1:
                memo[key] = False
                return False


            flag = False

            n = len(s1)

            for k in range(1, n):

                case1 = solve(s1[0:k], s2[n - k:n]) and solve(s1[k:], s2[0:n - k])
                case2 = solve(s1[0:k], s2[0:k]) and solve(s1[k:n], s2[k:n])

                if case1 or case2:
                    flag = True
                    break

            memo[key] = flag

            return memo[key]
        return solve(s1,s2)


def test1():
    sol=Solution()
    print(sol.isScramble("great","rgeat"))
