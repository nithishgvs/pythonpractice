from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = len(isConnected)
        sz = [1] * provinces
        id = [0] * provinces

        for i in range(provinces):
            id[i] = i

        def find(p):
            root = p
            while id[root] != root:
                root = id[root]
            while p != root:
                next = id[p]
                id[p] = root
                p = next
            return root

        def union(p, q):

            root1 = find(p)
            root2 = find(q)
            if root1 == root2:
                return False
            sz1 = sz[root1]
            sz2 = sz[root2]
            if sz1 < sz2:
                id[root1] = root2
                sz[root2] += sz1
            else:
                id[root2] = root1
                sz[root1] += sz2
            return True

        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if r != c and isConnected[r][c] == 1:
                    if union(r, c):
                        provinces -= 1
        return provinces


def test():
    s = Solution()
    print(s.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
