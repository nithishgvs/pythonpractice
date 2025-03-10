from tkinter.filedialog import dialogstates
from typing import Optional

from src.trees.tree_node import TreeNode


class DiameterOfBinaryTree:
    def __init__(self):
        self.max_depth = -1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.max_depth = max(self.max_depth, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.max_depth


def test_diameter():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    tree = DiameterOfBinaryTree()
    print(tree.diameterOfBinaryTree(root))
