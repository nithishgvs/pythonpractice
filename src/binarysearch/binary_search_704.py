from typing import List


class BinarySearch:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = l + (h - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1

        return -1;


def test_bs():
    object = BinarySearch();
    print(object.search([-1, 0, 3, 5, 9, 12], 92))
