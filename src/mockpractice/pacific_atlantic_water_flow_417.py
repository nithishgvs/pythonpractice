from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []

        rows = len(heights)
        cols = len(heights[0])

        atlantic = [[False] * cols for _ in range(rows)]
        pacific = [[False] * cols for _ in range(rows)]

        neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs1(ocean, r, cols, heights):

            for col in range(cols):
                dfs(ocean, r, col, heights)

        def dfs2(ocean, rows, col, heights):

            for row in range(rows):
                dfs(ocean, row, col, heights)

        def dfs(ocean, r, c, heights):

            if r < 0 or r >= rows or c < 0 or c >= cols or ocean[r][c]:
                return

            ocean[r][c] = True

            for neigh in neighbours:
                n_r = r + neigh[0]
                n_c = c + neigh[1]

                if n_r < 0 or n_r >= rows or n_c < 0 or n_c >= cols:
                    continue

                if heights[n_r][n_c] >= heights[r][c]:
                    dfs(ocean, n_r, n_c, heights)

        # pacific
        dfs1(pacific, 0, cols, heights)
        dfs2(pacific, rows, 0, heights)
        # atlantic
        dfs1(atlantic, rows-1, cols, heights)
        dfs2(atlantic, rows, cols-1, heights)

        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])
        return result
