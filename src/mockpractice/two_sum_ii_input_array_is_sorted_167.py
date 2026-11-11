class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, h = 0, len(numbers) - 1

        while l < h:
            if numbers[l] + numbers[h] == target:
                return [l + 1, h + 1]
            elif numbers[l] + numbers[h] < target:
                l += 1
            else:
                h -= 1


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([-1, 0], -1))
