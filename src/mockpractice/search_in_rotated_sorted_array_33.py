class Solution:
    def search(self, nums: list[int], target: int) -> int:
        ans = -1
        l, h = 0, len(nums) - 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                ans = mid
                break

            if nums[mid] <= nums[h]:
                # right sorted
                if nums[mid] <= target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
            else:
                # left sorted
                if nums[l] <= target <= nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1

        return ans


def test():
    s = Solution()
    # print(s.search([5, 1, 3], 5))
    #print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(s.search([3,1], 0))
