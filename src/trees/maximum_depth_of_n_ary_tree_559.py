from typing import Optional, List

from src.trees.n_ary_test_case_helper import TestHelper


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    max_depth = 0

    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        curr_max = 1
        for node in root.children:
            curr_max = max(curr_max, 1 + self.maxDepth(node))

        self.max_depth = max(self.max_depth, curr_max)
        return curr_max


def test():
    root = TestHelper().build_tree(
        [1, None, 3, 2, 4, None, 5, 6])
    s = Solution()
    print(s.maxDepth(root))
