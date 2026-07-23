from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        rows = len(nums1) + 1
        cols = len(nums2) + 1

        t = [[0] * cols for _ in range(rows)]
        max_length = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if nums1[r - 1] == nums2[c - 1]:
                    t[r][c] = 1 + t[r - 1][c - 1]
                    max_length = max(max_length, t[r][c])
        return max_length


def test1():
    s = Solution()
    print(s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
