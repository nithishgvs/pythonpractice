from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        num_islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    self.helper(i, j, rows, cols, grid)
                    num_islands += 1
        return num_islands

    def helper(self, i, j, rows, cols, grid):
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for n in neighbors:
            new_r = i + n[0]
            new_c = j + n[1]
            self.helper(new_r, new_c, rows, cols, grid)


def test():
    s = Solution()
    print(s.numIslands([["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]))
