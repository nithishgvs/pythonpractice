from typing import List


class TwoSum():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        result = []

        for index, num in enumerate(nums):
            if target - num in dictionary:
                result.append(dictionary[target - num])
                result.append(index)
                break
            else:
                dictionary[num] = index
        return result


def test_two_sum():
    two_sum = TwoSum()
    print(two_sum.twoSum([2, 7, 11, 15], 9))
