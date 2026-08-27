class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result: list[list[int]] = []

        start = 0
        n = len(nums)

        while start < n - 2:
            target = -1 * nums[start]

            l, h = start + 1, n - 1

            while l < h:

                curr_sum = nums[l] + nums[h]

                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    h -= 1
                else:
                    result.append([nums[start], nums[l], nums[h]])

                    while l < h and nums[l] == nums[l + 1]:
                        l += 1
                    while l < h and nums[h] == nums[h - 1]:
                        h -= 1
                    l += 1
                    h -= 1

                    while start < n-1 and nums[start] == nums[start + 1]:
                        start += 1
            start += 1

        return result


def test():
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
