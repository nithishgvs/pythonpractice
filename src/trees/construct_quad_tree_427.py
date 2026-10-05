from typing import List, Optional


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    # Time: O(n^2 log n) worst case because regions may be scanned at each level.
    # Space: O(n^2) for the quadtree, plus O(log n) recursion stack.
    def construct(self, grid: List[List[int]]) -> Optional[Node]:
        if not grid or not grid[0]:
            return None

        def dfs(row_start: int, col_start: int, row_end: int, col_end: int) -> Node:
            value = grid[row_start][col_start]

            # If every cell in this square matches, it becomes one leaf.
            is_uniform = True
            for row in range(row_start, row_end):
                for col in range(col_start, col_end):
                    if grid[row][col] != value:
                        is_uniform = False
                        break
                if not is_uniform:
                    break

            if is_uniform:
                return Node(value, True, None, None, None, None)

            mid_row = (row_start + row_end) // 2
            mid_col = (col_start + col_end) // 2

            return Node(
                1,
                False,
                dfs(row_start, col_start, mid_row, mid_col),
                dfs(row_start, mid_col, mid_row, col_end),
                dfs(mid_row, col_start, row_end, mid_col),
                dfs(mid_row, mid_col, row_end, col_end),
            )

        return dfs(0, 0, len(grid), len(grid[0]))
