from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def solve(index: int, curr_amount: int):

            if curr_amount == 0:
                return 0
            if index < 0:
                return float("inf")
            if (index, curr_amount) in dp:
                return dp[(index, curr_amount)]
            current_coin = coins[index]
            # 2 cases consider coin and not consider
            cant_take = solve(index - 1, curr_amount)
            if current_coin <= curr_amount:
                can_take = 1 + solve(index, curr_amount - current_coin)
                result = min(can_take, cant_take)
            else:
                result = cant_take
            dp[(index, curr_amount)] = result

            return result

        res = solve(len(coins) - 1, amount)

        return -1 if res == float("inf") else res


def test():
    sol = Solution()
    print (sol.coinChange([1, 2], 4))
