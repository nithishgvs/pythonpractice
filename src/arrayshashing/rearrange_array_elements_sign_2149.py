from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        result = [0 for _ in nums]
        pos_index = 0
        neg_index = 1

        for num in nums:

            if num < 0:
                result[neg_index] = num
                neg_index += 2
            else:
                result[pos_index] = num
                pos_index += 2

        return result


def test_rearrange():
    object = Solution()
    print(object.rearrangeArray([3, 1, -2, -5, 2, -4]))
