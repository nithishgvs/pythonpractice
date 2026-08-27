from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        l, h = 0, len(height) - 1

        while l < h:
            val1 = height[l]
            val2 = height[h]

            max_area = max(max_area, min(val1, val2) * (h - l))

            if val1 > val2:
                h -= 1
            elif val1 < val2:
                l += 1
            else:
                l += 1
                h -= 1
        return max_area


def test():
    sol = Solution()
    sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
