from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        total = 0
        queue = deque()
        neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    total += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        total_mins = 0
        while queue and total > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for row_offset, col_offset in neighbours:
                    r = i + row_offset
                    c = j + col_offset

                    if -1 < r < rows and -1 < c < cols:
                        if grid[r][c] == 1:
                            total -= 1
                            grid[r][c] = 2
                            queue.append((r, c))
            total_mins += 1

        return total_mins if total == 0 else -1


def test_1():
    solution = Solution()
    assert solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert solution.orangesRotting([[2]]) == 0
