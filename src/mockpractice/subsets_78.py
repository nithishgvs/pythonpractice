from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(i: int, curr_list: List[int] = []):
            result.append(curr_list.copy())

            for index in range(i, len(nums)):
                curr_list.append(nums[index])
                backtrack(index + 1, curr_list)
                curr_list.pop()

        backtrack(0, [])
        return result


def test():
    s = Solution()
    print(s.subsets([1, 2]))
