class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_buy)
            min_buy = min(min_buy, prices[i])
        return max_profit


def test():
    s = Solution()
    print(s.maxProfit([1]))
