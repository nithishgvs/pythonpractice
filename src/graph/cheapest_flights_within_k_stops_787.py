import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n

        prices[src] = 0

        for i in range(k + 1):
            tmp_array = prices.copy()

            for src, dest, price in flights:

                if prices[src] + price < tmp_array[dest]:
                    tmp_array[dest] = prices[src] + price
            prices = tmp_array

        return prices[dst] if prices[dst] != float("inf") else -1


def test1():
    sol = Solution()
    print(sol.findCheapestPrice(2, [[1,0,5]], 0, 1, 1))
    # print(sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
    # print(sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
    #print(sol.findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))
