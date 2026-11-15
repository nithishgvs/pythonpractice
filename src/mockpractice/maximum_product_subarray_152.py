# https://www.youtube.com/watch?v=lXVy6YWFcRM
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curr_max, curr_min = 1, 1
        res = nums[0]

        for n in nums:
            if n == 0:
                curr_max, curr_min = 1, 1
            else:
                tmp = curr_max * n
                curr_max = max(curr_max * n, curr_min * n, n)
                curr_min = min(tmp, curr_min * n, n)
                res = max(curr_max, res)
        return res


def test():
    s = Solution()
    print(s.maxProduct([-2, 0, -1]))
