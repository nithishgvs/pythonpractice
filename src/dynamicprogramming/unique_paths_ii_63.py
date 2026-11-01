class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = -1
        obstacleGrid[0][0] = 1

        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == -1:
                    continue
                if r - 1 >= 0 and obstacleGrid[r - 1][c] != -1:
                    obstacleGrid[r][c] += obstacleGrid[r - 1][c]
                if c - 1 >= 0 and obstacleGrid[r][c - 1] != -1:
                    obstacleGrid[r][c] += obstacleGrid[r][c - 1]

        return obstacleGrid[rows - 1][cols - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePathsWithObstacles([[0, 0], [0, 1]]))
