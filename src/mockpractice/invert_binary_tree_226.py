from src.trees.test_case_helper import TestHelper
from src.trees.tree_node import TreeNode


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root


def test():
    s = Solution()
    root = TestHelper().build_tree([1, 2, 3])
    print(s.invertTree(root))
