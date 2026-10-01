class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result: list[list[int]] = []

        for start in range(len(nums) - 2):
            if start > 0 and nums[start] == nums[start - 1]:
                continue

            l = start + 1
            h = len(nums) - 1
            target = -nums[start]

            while l < h:
                curr_sum = nums[l] + nums[h]
                if curr_sum == target:
                    result.append([nums[start], nums[l], nums[h]])
                    while l < h and nums[l] == nums[l + 1]:
                        l += 1
                    while l < h and nums[h] == nums[h - 1]:
                        h -= 1
                    l += 1
                    h -= 1
                elif curr_sum > target:
                    h -= 1
                else:
                    l += 1

        return result


def test_three_sum_returns_unique_triplets():
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [
        [-1, -1, 2],
        [-1, 0, 1],
    ]


def test_three_sum_does_not_repeat_triplets_for_repeated_anchor_values():
    assert Solution().threeSum([-1, -1, -1, 0, 1, 2]) == [
        [-1, -1, 2],
        [-1, 0, 1],
    ]
