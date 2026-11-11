class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def findRange(boolean_first: bool) -> int:
            l, h = 0, len(nums) - 1
            ans = -1
            while l <= h:
                mid = (l + h) // 2
                if nums[mid] == target:
                    ans = mid
                    if boolean_first:
                        h = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] > target:
                    h = mid - 1
                else:
                    l = mid + 1

            return ans

        return [findRange(True), findRange(False)]


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([2, 2, 2, 2, 2, 2], 2))
