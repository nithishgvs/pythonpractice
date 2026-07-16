from typing import List


def is_valid(result, n, row_index, col_index):
    # check if rows have the Queen
    for i in range(0, col_index):
        if result[row_index][i] == "Q":
            return False

    # upper-left diagonal (already-placed columns, rows above)
    i, j = row_index - 1, col_index - 1
    while i > -1 and j > -1:
        if result[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # lower-left diagonal (already-placed columns, rows below)
    i, j = row_index + 1, col_index - 1
    while i < n and j > -1:
        if result[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        temp_result = [["."] * n for _ in range(n)]

        result = []

        def backtrack(col):

            if col == n:
                result.append(["".join(row) for row in temp_result])
                return

            # Pick a row for this column, add the queen and move on to the next column
            for row_index in range(n):
                if is_valid(temp_result, n, row_index, col):
                    temp_result[row_index][col] = "Q"
                    backtrack(col + 1)
                    temp_result[row_index][col] = "."

        backtrack(0)

        return result


def test1():
    sol = Solution()
    print(sol.solveNQueens(4))
