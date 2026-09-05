from collections import deque
from typing import List, Optional, Deque

from src.trees.test_case_helper import TestHelper
from src.trees.tree_node import TreeNode


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue: deque[tuple[TreeNode, int, int]] = deque()
        tree_dict: dict[int, list[tuple[int, int]]] = {}

        queue.append((root, 0, 0))

        while queue:
            size = len(queue)

            for i in range(size):
                node, row_index, col_index = queue.popleft()

                tree_dict.setdefault(col_index, []).append((row_index, node.val))

                if node.left:
                    queue.append((node.left, row_index + 1, col_index - 1))
                if node.right:
                    queue.append((node.right, row_index + 1, col_index + 1))

        return [
            [value for row, value in sorted(tree_dict[col])]
            for col in sorted(tree_dict)
        ]


def test():
    test = TestHelper()
    root = test.build_tree([3, 9, 20, None, None, 15, 7])
    s = Solution()
    print(s.verticalTraversal(root))
