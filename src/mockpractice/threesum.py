class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        start = 0
        result: list[list[int]] = []

        while start < len(nums) - 2:

            if start > 0 and nums[start] == nums[start - 1]:
                start += 1
                continue

            l = start + 1
            h = len(nums) - 1

            while l < h:
                target = -1 * nums[start]
                if nums[l] + nums[h] == target:
                    result.append([nums[start], nums[l], nums[h]])
                    while l < h and nums[l] == nums[l + 1]:
                        l += 1
                    while l < h and nums[h] == nums[h - 1]:
                        h -= 1
                    l += 1
                    h -= 1
                elif nums[l] + nums[h] > target:
                    h -= 1
                else:
                    l += 1
            start += 1
        return result


def test():
    s = Solution()
    print(s.threeSum([0, 0, 0, 0]))
