class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        h = len(height) - 1
        max_area = 0

        while l < h:

            current = (h - l) * min(height[l], height[h])
            max_area = max(max_area, current)

            if height[l] < height[h]:
                l += 1
            elif height[l] > height[h]:
                h -= 1
            else:
                l += 1
                h -= 1
        return max_area


def test():
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
