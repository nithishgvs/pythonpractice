from src.trees.test_case_helper import TestHelper


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.count = 0

    def averageOfSubtree(self, root: TreeNode) -> int:

        self.dfs(root)
        return self.count

    def dfs(self, root):
        if root is None:
            return 0, 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        total_sum = left[0] + right[0] + root.val
        total_nodes = left[1] + right[1] + 1

        if root.val == (total_sum // total_nodes):
            self.count += 1

        return total_sum, total_nodes


if __name__ == "__main__":
    test = TestHelper()
    root = test.build_tree([1])
    object = Solution()
    print(object.averageOfSubtree(root))
