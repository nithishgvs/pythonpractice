from src.trees.tree_node import TreeNode


class Solution:

    def __init__(self):
        self.count = 0

    def helper(self, current_node: TreeNode, max_val):
        if current_node is None:
            return

        if current_node.val >= max_val:
            self.count += 1

        self.helper(current_node.left, max(current_node.val, max_val))
        self.helper(current_node.right, max(current_node.val, max_val))

    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return self.count

        self.helper(root, root.val)

        return self.count


def test_tree():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    object = Solution()
    print(object.goodNodes(root))
