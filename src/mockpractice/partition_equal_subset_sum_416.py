class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp: dict[tuple[int, int], bool] = {}

        def solve(index: int, remaining: int) -> bool:
            if remaining == 0:
                return True

            if index == 0 or remaining < 0:
                return False

            if (index, remaining) in dp:
                return dp[(index, remaining)]

            curr_value = nums[index - 1]

            if curr_value <= remaining:
                result = (solve(index - 1, remaining - curr_value)
                          or solve(index - 1, remaining))
            else:
                result = solve(index - 1, remaining)

            dp[(index, remaining)] = result
            return result

        return solve(len(nums), target)


def test():
    s = Solution()
    assert s.canPartition([1, 5, 11, 5]) is True
    assert s.canPartition([1, 2, 3, 5]) is False
    assert s.canPartition([1, 2, 5]) is False
