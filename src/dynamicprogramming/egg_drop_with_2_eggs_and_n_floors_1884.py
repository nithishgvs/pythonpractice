class Solution:
    def twoEggDrop(self, n: int) -> int:
        # Time: O(n^2) — O(n) floor states, each trying O(n) drop floors.
        # Space: O(n) — one memoized state for each floor count with two eggs.

        memo = {}

        def solve(n: int, e: int) -> int:

            if e == 1:
                return n
            if n == 0 or n == 1:
                return n

            if (n, e) in memo:
                return memo[(n, e)]

            moves = float("inf")

            for k in range(1, n + 1):
                temp = 1 + max(solve(k - 1, e - 1), solve(n - k, e))
                moves = min(temp, moves)

            memo[(n, e)] = moves
            return memo[(n, e)]

        return solve(n, 2)


def test():
    sol = Solution()
    print(sol.twoEggDrop(2))
