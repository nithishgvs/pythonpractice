from typing import List


class Solution:
    # Time:  O(9^m) worst case, where m is the number of empty cells
    #        (each empty cell tries up to 9 digits before backtracking).
    #        In practice the row/col/box pruning keeps this far lower.
    # Space: O(1) extra beyond the fixed 9x9 rows/cols/boxes sets and the
    #        recursion stack, which is bounded by 81 cells deep.
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # fill up the values in the beginning into the above matrices

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value != ".":
                    rows[r].add(value)
                    cols[c].add(value)
                    box_index = (r // 3) * 3 + (c // 3)
                    boxes[box_index].add(value)

        def backtrack(r: int, c: int) -> bool:
            # walked past the last row -> every cell filled, board solved
            if r == 9:
                return True

            next_r, next_c = (r, c + 1) if c < 8 else (r + 1, 0)

            # cell already given in the puzzle, nothing to choose here
            if board[r][c] != ".":
                return backtrack(next_r, next_c)

            box_index = (r // 3) * 3 + (c // 3)
            for value in "123456789":
                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in boxes[box_index]
                ):
                    continue

                # choose: place the digit and mark it as used
                board[r][c] = value
                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)

                if backtrack(next_r, next_c):
                    return True

                # un-choose: this digit didn't lead to a solution, revert
                # and let the loop try the next candidate digit
                board[r][c] = "."
                rows[r].remove(value)
                cols[c].remove(value)
                boxes[box_index].remove(value)

            # no digit worked for this cell, tell the caller to backtrack
            return False

        backtrack(0, 0)
