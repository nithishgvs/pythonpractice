class Solution:

    def subsets_dp(self, nums, target) -> int:
        rows = len(nums) + 1
        cols = target + 1

        t = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            t[r][0] = 1

        for r in range(1, rows):
            for c in range(1, cols):
                if nums[r - 1] <= c:
                    t[r][c] = t[r - 1][c] + t[r - 1][c - nums[r - 1]]
                else:
                    t[r][c] = t[r - 1][c]
        return t[rows - 1][cols - 1]

    def subsets(self, nums, target) -> int:

        dp = {}

        def subsets_mem(index, target):
            # With no numbers left, there is one subset for sum 0 (the empty
            # subset) and no subset for any other target.
            if index == 0:
                return 1 if target == 0 else 0

            if (index, target) in dp:
                return dp[(index, target)]

            if nums[index - 1] <= target:
                # number is less than the target so we can or can't consider
                result = subsets_mem(index - 1, target - nums[index - 1]) + subsets_mem(index - 1, target)
            else:
                result = subsets_mem(index - 1, target)

            dp[(index, target)] = result
            return result

        return subsets_mem(len(nums), target)


def test():
    s = Solution()
    print(s.subsets_dp([1, 2, 3], 6))
