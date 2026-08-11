class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # Time: O(k * n * log n); Space: O(k * n) for memoization.
        memo = {}

        def solve(e: int, n: int) -> int:
            if e == 1:
                return n
            if n == 0 or n == 1:
                return n

            if (e, n) in memo:
                return memo[(e, n)]

            low, high = 1, n
            moves = float("inf")

            # As the drop floor rises, the break case increases and the
            # survive case decreases. Binary-search their balance point.
            while low <= high:
                floor = (low + high) // 2
                breaks = solve(e - 1, floor - 1)
                survives = solve(e, n - floor)
                moves = min(moves, 1 + max(breaks, survives))

                if breaks > survives:
                    high = floor - 1
                else:
                    low = floor + 1

            memo[(e, n)] = moves

            return moves

        return solve(k, n)


def test():
    sol = Solution()
    print(sol.superEggDrop(3, 14))
