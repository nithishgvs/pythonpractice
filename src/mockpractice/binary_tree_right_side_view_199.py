from collections import deque

from src.trees.test_case_helper import TestHelper
from src.trees.tree_node import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        result: list[int] = []

        if root is None:
            return result

        q: deque[TreeNode] = deque()
        q.append(root)

        while q:
            size = len(q)

            for index in range(size):
                pop = q.popleft()
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
                if index == size - 1:
                    result.append(pop.val)
        return result


def test():
    s = Solution()
    root = TestHelper().build_tree([1, 2, 3, 4, None, None, None, 5])
    print(s.rightSideView(root))