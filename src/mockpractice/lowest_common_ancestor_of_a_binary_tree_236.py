from src.trees.test_case_helper import TestHelper
from src.trees.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if root is None:
            return None

        if root == p or root == q:
            return root

        right = self.lowestCommonAncestor(root.right, p, q)
        left = self.lowestCommonAncestor(root.left, p, q)
        if left and right:
            return root

        return left or right


def test():
    s = Solution()
    root = TestHelper().build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(s.lowestCommonAncestor(root, root.left, root.left.right.right).val)
