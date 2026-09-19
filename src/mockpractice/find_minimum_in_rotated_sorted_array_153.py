class Solution:
    def findMin(self, nums: list[int]) -> int:

        l, h = 0, len(nums) - 1

        while l < h:
            mid = (l + h) // 2

            if nums[mid] < nums[h]:
                # right side is sorted
                h = mid
            else:
                l = mid + 1
        return nums[l]


def test():
    s = Solution()
    print(s.findMin([3, 1, 2]))
    print(s.findMin([11, 13, 15, 17]))
    print(s.findMin([11, 13, 15, 17]))
