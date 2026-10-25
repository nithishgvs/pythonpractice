class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def solve(sr, sc):
            visited.add((sr, sc))
            for n in neighbors:
                nr = sr + n[0]
                nc = sc + n[1]
                if nr < 0 or nr >= len(image) or nc < 0 or nc >= len(image[0]) or (nr, nc) in visited:
                    continue
                if image[nr][nc] == image[sr][sc]:
                    solve(nr, nc)

        solve(sr, sc)
        for (sr, sc) in visited:
            image[sr][sc] = color
        return image


def test():
    s = Solution()
    print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
