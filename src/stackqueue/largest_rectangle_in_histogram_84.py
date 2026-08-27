from typing import List

#https://www.youtube.com/watch?v=zx5Sw9130L0
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0

        stack = []

        for idx, height in enumerate(heights):

            if not stack or stack[-1][1] <= height:
                stack.append((idx, height))
            else:
                prev_idx = 0
                while stack and stack[-1][1] > height:
                    prev_idx = stack[-1][0]
                    prev_height = stack[-1][1]
                    curr_area = (idx - prev_idx) * prev_height
                    stack.pop()
                    max_area = max(max_area, curr_area)
                stack.append((prev_idx, height))

        while stack:
            idx, height = stack.pop()
            curr_area = (len(heights) - idx) * height
            max_area = max(max_area, curr_area)

        return max_area


def test():
    obj = Solution()
    print(obj.largestRectangleArea([2, 1, 5, 6, 2, 3]))
