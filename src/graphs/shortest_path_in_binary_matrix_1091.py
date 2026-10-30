from collections import deque
from typing import Deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        directions = [[1, 1], [-1, -1], [0, -1], [-1, 1], [-1, 0], [0, 1], [1, -1], [1, 0]]

        queue = deque()

        queue.append((0, 0))

        visited = set()

        path = 1

        while queue:
            size = len(queue)

            for _ in range(size):
                r, c = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    return path

                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 1 or (nr, nc) in visited:
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            path += 1
        return -1


def test():
    s = Solution()
    print(s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
