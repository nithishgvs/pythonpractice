from typing import Optional, List

from src.trees.n_ary_test_case_helper import TestHelper


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result: List[int] = []

        if root is None:
            return result

        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.children:
                stack.extend(reversed(node.children))
        return result

    def preorder_recursive(self, root: 'Node') -> List[int]:
        result: List[int] = []

        def dfs(root: Node):

            if not root:
                return

            result.append(root.val)

            for node in root.children:
                dfs(node)

        dfs(root)
        return result


def test():
    root = TestHelper().build_tree(
        [1, None, 3, 2, 4, None, 5, 6])
    s = Solution()
    print(s.preorder(root))
