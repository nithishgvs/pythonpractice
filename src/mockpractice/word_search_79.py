from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = [[False] * cols for _ in range(rows)]

        def solve(index: int, r: int, c: int):
            if index == len(word):
                return True

            if r < 0 or r >= rows or c >= cols or c < 0 or visited[r][c]:
                return False

            if board[r][c] != word[index]:
                return False
            visited[r][c] = True
            found = (solve(index + 1, r + neighbors[0][0], c + neighbors[0][1]) or
                     solve(index + 1, r + neighbors[1][0], c + neighbors[1][1]) or
                     solve(index + 1, r + neighbors[2][0], c + neighbors[2][1]) or
                     solve(index + 1, r + neighbors[3][0], c + neighbors[3][1]))
            visited[r][c] = False
            return found

        for i in range(rows):
            for j in range(cols):
                if solve(0, i, j):
                    return True
        return False


def test():
    s = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(s.exist(board, word))


def test1():
    s = Solution()
    board = [["A"]]
    word = "A"
    print(s.exist(board, word))
