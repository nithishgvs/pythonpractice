from typing import Optional

from src.trees.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.count = 0
        self.result = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(root: Optional[TreeNode], k: int) -> int:
            if not root:
                return

            inorder(root.left, k)
            self.count += 1
            if self.count == k:
                self.result = root.val
                return
            inorder(root.right, k)

        inorder(root, k)
        return self.result


def test_kth():
    """
            Creates the following BST:
                    5
                   / \
                  3   7
                 / \   \
                2   4   8
               /
              1
            """
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(8)
    root.left.left.left = TreeNode(1)

    tree = Solution()
    print(tree.kthSmallest(root, 2))
