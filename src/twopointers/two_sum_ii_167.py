from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, h = 0, len(numbers) - 1

        while l < h:
            curr_sum = numbers[l] + numbers[h]
            if curr_sum == target:
                return [l+1, h+1]
            elif curr_sum > target:
                h -= 1
            else:
                l += 1


def test1():
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
