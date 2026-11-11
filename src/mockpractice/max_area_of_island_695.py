class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        max_island = float("-inf")

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            value = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            return value

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_island = max(max_island, dfs(r, c))
        return 0 if max_island == float("-inf") else max_island


def test():
    s = Solution()
    print(s.maxAreaOfIsland([[0, 1, 1, 0],
                             [0, 1, 0, 0],
                             [1, 0, 0, 1],
                             [0, 0, 1, 1]]))
