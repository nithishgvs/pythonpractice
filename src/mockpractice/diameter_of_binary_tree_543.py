from typing import Optional

from src.trees.test_case_helper import TestHelper
from src.trees.tree_node import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if root is None:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)

            max_diameter = max(max_diameter, left_max + right_max)
            return 1 + max(left_max, right_max)

        dfs(root)
        return max_diameter


def test():
    s = Solution()
    root = TestHelper().build_tree([1, 2, 3, 4, 5])
    print(s.diameterOfBinaryTree(root))
