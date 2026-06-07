from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row = len(heights)
        col = len(heights[0])

        pacific = [[False] * col for _ in range(row)]
        atlantic = [[False] * col for _ in range(row)]
        result = []

        neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # pacific
        self.dfs1(col, heights, neighbours, pacific, row, 0)
        self.dfs2(col, heights, neighbours, pacific, row, 0)

        # atlantic
        self.dfs1(col, heights, neighbours, atlantic, row, row - 1)
        self.dfs2(col, heights, neighbours, atlantic, row, col - 1)

        for i in range(row):
            for j in range(col):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])

        return result

    def dfs(self, curr_row, curr_col, neighbours, ocean, row, col, heights):
        ocean[curr_row][curr_col] = True
        for n in neighbours:
            n_r = curr_row + n[0]
            n_c = curr_col + n[1]
            if (
                -1 < n_r < row
                and -1 < n_c < col
                and not ocean[n_r][n_c]
                and heights[n_r][n_c] >= heights[curr_row][curr_col]
            ):
                self.dfs(n_r, n_c, neighbours, ocean, row, col, heights)

    def dfs1(self, col, heights, neighbours, ocean, row, r):
        for j in range(col):
            self.dfs(r, j, neighbours, ocean, row, col, heights)

    def dfs2(self, col, heights, neighbours, ocean, row, c):
        for i in range(row):
            self.dfs(i, c, neighbours, ocean, row, col, heights)


def test_1():
    solution = Solution()
    result = solution.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
    assert sorted(result) == sorted([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
