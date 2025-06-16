from typing import List


def dfs(row_idx, col_idx, rows, cols, idx, word, visited, board):
    if row_idx >= rows or col_idx >= cols or row_idx < 0 or col_idx < 0:
        return False

    if visited[row_idx][col_idx] or board[row_idx][col_idx] != word[idx]:
        return False

    if idx == len(word) - 1:
        return True

    visited[row_idx][col_idx] = True
    found = (
            dfs(row_idx - 1, col_idx, rows, cols, idx + 1, word, visited, board) or
            dfs(row_idx, col_idx - 1, rows, cols, idx + 1, word, visited, board) or
            dfs(row_idx + 1, col_idx, rows, cols, idx + 1, word, visited, board) or
            dfs(row_idx, col_idx + 1, rows, cols, idx + 1, word, visited, board)
    )
    visited[row_idx][col_idx] = False
    return found


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        for row_idx, row in enumerate(board):
            for col_idx, value in enumerate(row):
                if dfs(row_idx, col_idx, rows, cols, 0, word, visited, board):
                    return True

        return False


def test_word_search():
    object = Solution()
    grid = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    print(object.exist(grid, "ABCCED"))
