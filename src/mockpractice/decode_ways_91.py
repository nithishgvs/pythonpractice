from itertools import count
from linecache import cache


class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def solve(index: int):
            if index == len(s):
                return 1
            if s[index] == 0:
                return 0

            count = solve(index + 1)

            if index + 1 < len(s) and 10 <= int(s[index:index + 2]) <= 26:
                count += solve(index + 2)
            return count

        return solve(0)


def test():
    s = Solution()
    s.numDecodings("226")
