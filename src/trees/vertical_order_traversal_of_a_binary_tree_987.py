from collections import deque
from typing import List, Optional, Deque

from src.trees.test_case_helper import TestHelper
from src.trees.tree_node import TreeNode


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue: deque[tuple(int, int, TreeNode)] = deque()
        tree_dict: dict[int, list[tuple[int, int]]] = {}

        queue.append((0, 0, root))

        while queue:
            size = len(queue)

            for _ in range(size):
                row, col, node = queue.popleft()
                tree_dict.setdefault(col, []).append((row, node.val))

                if node.left:
                    queue.append((row + 1, col - 1, node.left))
                if node.right:
                    queue.append((row + 1, col + 1, node.right))

        return [[val for row,val in sorted(tree_dict[val])] for val in sorted(tree_dict)]


def test():
    test = TestHelper()
    root = test.build_tree([3, 9, 20, None, None, 15, 7])
    s = Solution()
    print(s.verticalTraversal(root))
