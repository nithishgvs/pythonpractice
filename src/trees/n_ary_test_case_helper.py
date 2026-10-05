from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class TestHelper:
    def build_tree(self, values):
        if not values:
            return None

        root = Node(values[0], [])
        queue = deque([root])
        parent = None

        for value in values[1:]:
            if value is None:
                parent = queue.popleft() if queue else None
                continue

            child = Node(value, [])
            if parent is None:
                raise ValueError("Invalid n-ary level-order input: child appears before a parent separator")
            parent.children.append(child)
            queue.append(child)

        return root
