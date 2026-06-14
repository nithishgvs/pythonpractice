from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = [-1] * len(nums1)
        stack = []
        nums1_index = {}

        for idx, n in enumerate(nums1):
            nums1_index[n] = idx

        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()

            if nums2[i] in nums1_index and stack:
                result[nums1_index[nums2[i]]] = stack[-1]

            stack.append(nums2[i])

        return result


def test_1():
    solution = Solution()
    assert solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert solution.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
    assert solution.nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]) == [7, 7, 7, 7, 7]
