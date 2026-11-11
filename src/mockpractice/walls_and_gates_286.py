from collections import deque


class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:

            r, c = queue.popleft()
            for d in directions:
                n_r, n_c = r + d[0], c + d[1]
                if (
                        n_r < 0 or n_r >= rows
                        or n_c < 0 or n_c >= cols
                        or rooms[n_r][n_c] != 2147483647
                ):
                    continue
                rooms[n_r][n_c] = rooms[r][c] + 1
                queue.append((n_r, n_c))


def test():
    s = Solution()
    s.wallsAndGates(
        [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1],
         [0, -1, 2147483647, 2147483647]])
