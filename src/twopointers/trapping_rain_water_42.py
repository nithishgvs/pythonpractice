from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        max_water = 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        curr_left_max = 0
        curr_right_max = 0

        for i in range(0, n):
            left_max[i] = curr_left_max
            curr_left_max = max(height[i], curr_left_max)

        for i in range(n - 1, -1, -1):
            right_max[i] = curr_right_max
            curr_right_max = max(height[i], curr_right_max)

        for i in range(1, n):
            max_water += max(0, min(left_max[i], right_max[i]) - height[i])

        return max_water


def test():
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
