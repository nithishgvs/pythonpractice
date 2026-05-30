from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')

        nums.sort()

        start = 0

        while start < len(nums) - 2:

            l = start + 1
            h = len(nums) - 1

            while l < h:
                curr_sum = nums[start] + nums[l] + nums[h]

                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum

                if curr_sum == target:
                    return closest
                elif curr_sum > target:
                    h = h - 1
                else:
                    l = l + 1
            start = start + 1

        return closest


def test_threesum():
    object = Solution()
    print(object.threeSumClosest([-1, 2, 1, -4], 1))
