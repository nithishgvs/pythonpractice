from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1

        while l < h:

            mid = l + (h - l) // 2

            if nums[mid] < nums[h]:
                h = mid
            else:
                l = mid + 1
        return nums[l]


def test():
    sol = Solution()
    print(sol.findMin([3, 1, 2]))
