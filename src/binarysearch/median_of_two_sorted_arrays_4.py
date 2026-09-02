from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            # always nums1 should be smaller we do binary search on this one
            nums2, nums1 = nums1, nums2

        l1 = len(nums1)
        l2 = len(nums2)

        l, h = 0, len(nums1) - 1

        # odd number so we add one so that left partition will have one extra element that becomes our median
        left_partition = (l2 + l1 + 1) // 2

        while True:
            mid = l + (h - l) // 2
            nums2_partition = left_partition - (mid + 2)

            nums1_left = nums1[mid] if mid >= 0 else float("-inf")
            nums1_right = nums1[mid + 1] if mid + 1 < l1 else float("inf")
            nums2_left = nums2[nums2_partition] if nums2_partition >= 0 else float("-inf")
            nums2_right = nums2[nums2_partition + 1] if nums2_partition + 1 < l2 else float("inf")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:

                # odd case
                if (l1 + l2) % 2:
                    return max(nums1_left, nums2_left)

                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                h = mid - 1
            else:
                l = mid + 1


def test1():
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7]))
