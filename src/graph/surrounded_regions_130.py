from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # upper border i=0
        for j in range(cols):
            self.dfs(visited, 0, j, board, rows, cols, neighbours)
        # lower border i=rows-1
        for j in range(cols):
            self.dfs(visited, rows - 1, j, board, rows, cols, neighbours)
        # right border j=cols-1
        for i in range(rows):
            self.dfs(visited, i, cols - 1, board, rows, cols, neighbours)
        # left border j=0
        for i in range(rows):
            self.dfs(visited, i, 0, board, rows, cols, neighbours)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "*":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    def dfs(self, visited, row, col, board, rows, cols, neighbours):
        if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or board[row][col] == "X":
            return

        visited[row][col] = True
        board[row][col] = "*"
        for neigh in neighbours:
            next_row = row + neigh[0]
            next_col = col + neigh[1]
            self.dfs(visited, next_row, next_col, board, rows, cols, neighbours)


def test_1():
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]

    Solution().solve(board)

    assert board == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]
