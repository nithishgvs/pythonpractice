class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        curr_sum = 0
        start = 0

        min_len = float("inf")

        for i in range(0, len(nums)):
            curr_sum += nums[i]

            while curr_sum >= target:
                min_len = min(min_len, i - start + 1)
                curr_sum -= nums[start]
                start += 1
        return 0 if min_len == float("inf") else min_len


def test():
    s = Solution()
    print(s.minSubArrayLen(4, [1, 4, 4]))
