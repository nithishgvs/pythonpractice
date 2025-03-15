from collections import deque
from typing import Optional, List

from src.trees.tree_node import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        result = []

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if _ == (size - 1):
                    result.append(node.val)
        return result


def test_level():
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))
    solution = Solution()
    print(solution.rightSideView(root))
