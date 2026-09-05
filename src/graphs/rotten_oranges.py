from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        number_fresh = 0

        q = deque()

        min_minutes = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    number_fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        if number_fresh == 0:
            return min_minutes

        while q:
            size = len(q)

            for i in range(size):

                popped = q.popleft()

                for n in neighbours:
                    new_r = popped[0] + n[0]
                    new_c = popped[1] + n[1]

                    if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols or grid[new_r][new_c] == 0 or \
                            grid[new_r][new_c] == 2:
                        continue
                    grid[new_r][new_c] = 2
                    number_fresh -= 1
                    q.append((new_r, new_c))

            min_minutes += 1
            if number_fresh == 0:
                return min_minutes

        return -1 if number_fresh != 0 else min_minutes


def test():
    s = Solution()
    print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
