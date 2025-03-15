from collections import deque
from typing import List, Optional

from src.trees.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None

        queue = deque([root])

        result = []

        while queue:
            current_list = []

            for i in range(len(queue)):
                item = queue.popleft()
                current_list.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            result.append(current_list)

        return result


def test_level():
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))
    solution = Solution()
    print(solution.levelOrder(root))
