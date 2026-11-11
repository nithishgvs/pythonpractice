class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0

        for i, jump in enumerate(nums):

            if i > farthest:
                return False

            farthest = max(farthest, i + jump)

            if farthest >= len(nums) - 1:
                return True

        return True


def test():
    s = Solution()
    print(s.canJump([3, 2, 1, 0, 4]))
