from typing import List


def dfs(row_idx, col_idx, rows, cols, grid):
    if row_idx < 0 or col_idx < 0 or col_idx >= cols or row_idx >= rows:
        return 0

    if grid[row_idx][col_idx] == 0:
        return 0

    grid[row_idx][col_idx] = 0

    return (
            1
            + dfs(row_idx + 1, col_idx, rows, cols, grid)
            + dfs(row_idx - 1, col_idx, rows, cols, grid)
            + dfs(row_idx, col_idx + 1, rows, cols, grid)
            + dfs(row_idx, col_idx - 1, rows, cols, grid)
    )


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0


        rows = len(grid)
        cols = len(grid[0])

        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                max_area = max(dfs(row_idx, col_idx, rows, cols, grid), max_area)

        return max_area


def test_max_area():
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]];
    object = Solution()
    print(object.maxAreaOfIsland(grid))
