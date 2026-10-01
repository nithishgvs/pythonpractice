class Solution:
    def trap(self, height: list[int]) -> int:
        length = len(height)
        left_max = [0] * length
        right_max = [0] * length

        curr_left_max = 0
        curr_right_max = 0

        max_trapped = 0

        for i in range(length):
            left_max[i] = curr_left_max
            curr_left_max = max(height[i], curr_left_max)

        for i in range(length - 1, -1, -1):
            right_max[i] = curr_right_max
            curr_right_max = max(height[i], curr_right_max)

        for i in range(length):
            max_trapped += max(0, min(left_max[i], right_max[i]) - height[i])

        return max_trapped


def test():
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
