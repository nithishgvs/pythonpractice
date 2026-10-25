class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:

        size = len(edges)
        id = [0] * size
        sz = [1] * size

        for i in range(size):
            id[i] = i

        def find(p) -> int:
            root = p
            while id[root] != root:
                root = id[root]
            while p != root:
                next = id[p]
                id[p] = root
                p = next
            return root

        def union(p, q) -> bool:

            root1 = find(p)
            root2 = find(q)

            if root1 == root2:
                return False

            if sz[root1] < sz[root2]:
                sz[root2] += sz[root1]
                id[root1] = root2
            else:
                sz[root1] += sz[root2]
                id[root2] = root1
            return True

        for e in edges:
            if not union(e[0] - 1, e[1] - 1):
                return e
        return []


def test():
    s = Solution()
    print(s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # expect [2, 3]
    print(s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # expect [1, 4]
