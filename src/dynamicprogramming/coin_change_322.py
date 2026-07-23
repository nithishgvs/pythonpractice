from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        rows = len(coins) + 1
        cols = amount + 1

        t = [[float("inf")] * cols for _ in range(rows)]

        t[0][0] = 0

        for r in range(1, rows):
            coin = coins[r - 1]
            for c in range(cols):
                if coin <= c:
                    t[r][c] = min(t[r - 1][c], 1 + t[r][c - coin])
                else:
                    t[r][c] = t[r - 1][c]
        return -1 if t[rows - 1][cols - 1] == float("inf") else t[rows - 1][cols - 1]

    def coinChange1(self, coins: List[int], amount: int) -> int:
        dp = {}

        def coin_recursion(n: int, amount: int) -> int:
            # Base condition
            if amount == 0:
                return 0
            if n == 0:
                return float("inf")

            if (n, amount) in dp:
                return dp[(n, amount)]

            coin = coins[n - 1]

            cant_take = coin_recursion(n - 1, amount)
            if coin <= amount:
                # can or cant consider
                result = min(cant_take, 1 + coin_recursion(n, amount - coin))
            else:
                result = cant_take

            dp[(n, amount)] = result

            return result

        result = coin_recursion(len(coins), amount)
        return -1 if result == float("inf") else result


def test():
    sol = Solution()
    print(sol.coinChange([2], 3))
