from collections import deque
from typing import Optional, List

from src.trees.n_ary_test_case_helper import TestHelper


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result: List[List[int]] = []

        if not root:
            return result

        queue: deque[Node] = deque([root])

        while queue:
            size = len(queue)
            curr_list: List[int] = []
            for _ in range(size):
                popped = queue.popleft()
                curr_list.append(popped.val)
                if popped.children:
                    queue.extend(popped.children)
            result.append(curr_list)
        return result


def test():
    root = TestHelper().build_tree(
        [1, None, 3, 2, 4, None, 5, 6])
    s = Solution()
    print(s.levelOrder(root))
