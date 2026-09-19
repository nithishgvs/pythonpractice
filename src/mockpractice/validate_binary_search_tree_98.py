from src.trees.test_case_helper import TestHelper
from src.trees.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def helper(min: float, max: float, root: TreeNode):

            if root is None:
                return True

            if root.val <= min or root.val >= max:
                return False

            return helper(min, root.val, root.left) and helper(root.val, max, root.right)

        return helper(float("-inf"), float("inf"), root)


def test():
    s = Solution()
    root = TestHelper().build_tree([2, 2, 2])
    print(s.isValidBST(root))
