class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []

        nums.sort()

        start = 0

        while start < len(nums) - 2:
            target_sum = -nums[start]

            l = start + 1
            h = len(nums) - 1

            while l < h:
                total = nums[l] + nums[h]

                if total > target_sum:
                    h = h - 1
                elif total < target_sum:
                    l = l + 1
                else:
                    result.append([nums[start], nums[l], nums[h]])

                    # remove duplicates
                    while l < h and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < h and nums[h] == nums[h - 1]:
                        h = h - 1

                    l = l + 1
                    h = h - 1

            start = start + 1
            # skip duplicate start values after incrementing
            while start < len(nums) - 2 and nums[start] == nums[start - 1]:
                start = start + 1

        return result


def test_threesum():
    object = Solution()
    print(object.threeSum([-1, 0, 1, 2, -1, -4]))
