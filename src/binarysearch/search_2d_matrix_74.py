from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1

        while top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                break

        if not (top <= bot):
            return False

        row = (top + bot) // 2

        l, r = 0, cols - 1

        while l <= r:

            mid = (l + r) // 2

            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True

        return False


def test_search():
    object = Solution()
    matrix =[[1,3]]
    print(object.searchMatrix(matrix, 3))
