from typing import Optional, List

from src.trees.n_ary_test_case_helper import TestHelper


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        result: List[int] = []

        if not root:
            return result

        stack = [root]

        while stack:
            popped = stack.pop()
            result.append(popped.val)
            stack.extend(popped.children)

        return result[::-1]

    def postorder_rec(self, root: 'Node') -> List[int]:

        result: List[int] = []

        def dfs(root: 'Node'):

            if not root:
                return
            for node in root.children:
                dfs(node)
            result.append(root.val)

        dfs(root)

        return result


def test():
    root = TestHelper().build_tree(
        [1, None, 3, 2, 4, None, 5, 6])
    s = Solution()
    print(s.postorder(root))
