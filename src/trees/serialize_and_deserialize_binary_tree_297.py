from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result=""
        def solve(root: TreeNode):
            nonlocal result
            if root is None:
                result += "#"
                result += ","
                return result

            result += str(root.val) + ","
            solve(root.left)
            solve(root.right)
            return result

        return solve(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = deque()
        split = data.split(",")
        for s in split:
            queue.append(s)

        def solve():
            popped = queue.popleft()
            if popped == "#":
                return None

            root = TreeNode(int(popped))

            root.left = solve()
            root.right = solve()

            return root

        return solve()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


if __name__ == "__main__":
    ser = Codec()
    """
                Creates the following BST:
                        5
                       / \
                      3   7
                     / \   \
                    2   4   8
                """
    root = TreeNode(5)
    root.left = TreeNode(3)
    # root.right = TreeNode(7)
    # root.left.left = TreeNode(2)
    # root.left.right = TreeNode(4)
    # root.right.right = TreeNode(8)
    # root.left.left.left = TreeNode(1)
    # print(ser.serialize(root))
    print(ser.deserialize(ser.serialize(root)))
