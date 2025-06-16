from typing import List


def dfs(row, col, grid, cols, rows):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return
    if grid[row][col] == '0':
        return

    grid[row][col] = '0'
    dfs(row + 1, col, grid, cols, rows)
    dfs(row - 1, col, grid, cols, rows)
    dfs(row, col + 1, grid, cols, rows)
    dfs(row, col - 1, grid, cols, rows)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        if len(grid) == 0:
            return num_islands

        rows = len(grid)
        cols = len(grid[0])

        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if grid[row_idx][col_idx] == '1':
                    num_islands += 1
                    dfs(row_idx, col_idx, grid, cols, rows)

        return num_islands


def test_num_islands():
    object = Solution()
    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]
    print(object.numIslands(grid))
