from collections import deque

from src.trees.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        result: list[list[int]] = []
        q: deque[TreeNode] = deque()
        if root:
            q.append(root)

        while q:
            size = len(q)
            current = []
            for _ in range(size):
                pop = q.popleft()
                current.append(pop.val)
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
            result.append(current)
        return result


def test():
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))
    solution = Solution()
    print(solution.levelOrder(root))
