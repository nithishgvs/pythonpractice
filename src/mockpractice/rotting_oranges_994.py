from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        total_fresh = 0
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    total_fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        total_mins = 0

        if total_fresh == 0:
            return total_mins

        neigh = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for n in neigh:
                    new_r = i + n[0]
                    new_c = j + n[1]

                    if -1 < new_r < rows and -1 < new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        total_fresh -= 1
                        queue.append((new_r, new_c))
            if len(queue) == 0 and total_fresh == 0:
                return total_mins
            total_mins += 1

        return -1


def test():
    s = Solution()
    print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
