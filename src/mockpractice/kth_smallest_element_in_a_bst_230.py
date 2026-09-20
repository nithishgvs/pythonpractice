from src.trees.test_case_helper import TestHelper
from src.trees.tree_node import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        res = -1

        def inorder(current_node: TreeNode | None):
            nonlocal k, res
            if current_node is None or k == 0:
                return

            inorder(current_node.left)
            if k == 0:
                return

            k -= 1
            if k == 0:
                res = current_node.val
                return

            inorder(current_node.right)

        inorder(root)
        return res


def test():
    s = Solution()
    root = TestHelper().build_tree([5, 3, 6, 2, 4, None, None, 1])
    print(s.kthSmallest(root, 3))
