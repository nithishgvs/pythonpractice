from typing import List


class Solution:

    def __init__(self):
        self.total = 0

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.total = 0

        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0 or visited[i][j]:
                return

            visited[i][j] = True

            self.total += 4

            for neigh in neighbours:
                n_r = i + neigh[0]
                n_c = j + neigh[1]

                if -1 < n_r < rows and -1 < n_c < cols and grid[n_r][n_c] == 1:
                    self.total -= 1

            for neigh in neighbours:
                dfs(i + neigh[0], j + neigh[1])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)

        return self.total


def test_1():
    solution = Solution()
    assert solution.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16
    assert solution.islandPerimeter([[1]]) == 4
