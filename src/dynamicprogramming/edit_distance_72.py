from linecache import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def solve(index1: int, index2: int) -> int:
            if index1 == 0:
                return index2
            if index2 == 0:
                return index1

            if (index1, index2) in dp:
                return dp[(index1, index2)]
            # knapsack
            result = 0
            if word1[index1 - 1] == word2[index2 - 1]:
                result = solve(index1 - 1, index2 - 1)
            else:
                delete = solve(index1 - 1, index2)
                insert = solve(index1, index2 - 1)
                replace = solve(index1 - 1, index2 - 1)
                result = min(delete, insert, replace) + 1

            dp[(index1, index2)] = result

            return result

        return solve(len(word1), len(word2))


def test():
    s = Solution()
    print(s.minDistance("horse", "ros"))
