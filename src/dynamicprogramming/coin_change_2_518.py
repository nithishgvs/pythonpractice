from typing import List


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:

        # Time: O(len(coins) * amount); Space: O(len(coins) * amount).
        # Each table cell represents the number of ways to form an amount using
        # the first `row` coin types.

        rows = len(coins) + 1
        cols = amount + 1

        t = [[0] * cols for _ in range(rows)]

        t[0][0] = 1

        for row in range(1, rows):
            coin = coins[row - 1]
            for col in range(cols):
                if coin <= col:
                    t[row][col] = t[row - 1][col] + t[row][col - coin]
                else:
                    t[row][col] = t[row - 1][col]

        return t[rows - 1][cols - 1]

    def change1(self, amount: int, coins: List[int]) -> int:

        # Time: O(len(coins) * amount); Space: O(len(coins) * amount) for memoization.
        # The recursion stack can additionally grow to O(amount / min(coins) + len(coins)).

        dp = {}

        def change_recursion(amount: int, n: int) -> int:

            if amount == 0:
                # reached the amount wanted
                return 1

            if n == 0:
                return 0

            if (amount, n) in dp:
                return dp[(amount, n)]

            coin = coins[n - 1]

            if coin <= amount:
                # can take or cant take
                result = change_recursion(amount - coin, n) + change_recursion(amount, n - 1)
            else:
                result = change_recursion(amount, n - 1)

            dp[(amount, n)] = result

            return result

        return change_recursion(amount, len(coins))


def test():
    s = Solution()
    print(s.change(5, [1, 2, 5]))
