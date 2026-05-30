from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        # Treat the matrix as a flat sorted array; map 1D index -> 2D with mid//cols, mid%cols
        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid // cols][mid % cols]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False


def test_search():
    sol = Solution()
    matrix = [[1, 3]]
    print(sol.searchMatrix(matrix, 3))
