class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # we go through all borders and if the value is not

        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or board[r][c] == "X":
                return
            visited[r][c] = True
            board[r][c] = "*"

            for n in neighbours:
                dfs(r + n[0], c + n[1])

        for c in range(cols):
            dfs(0, c)
        for c in range(cols):
            dfs(rows - 1, c)
        for r in range(rows):
            dfs(r, 0)
        for r in range(rows):
            dfs(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                print(board[r][c])
                if board[r][c] == "*":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"


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
