class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones: dict[Node, Node] = {}

        def clone(node: Optional['Node']):
            if node is None:
                return None
            if node in clones:
                return clones[node]

            clone_node = Node(node.val, [])
            clones[node] = clone_node

            for nei in node.neighbors:
                new_node = clone(nei)
                clone_node.neighbors.append(new_node)
            return clone_node

        return clone(node)


def test():
    node1 = Node(1)

    node2 = Node(2)

    node3 = Node(3)

    node4 = Node(4)

    # Build graphs:

    # adjList = [[2,4],[1,3],[2,4],[1,3]]

    node1.neighbors = [node2, node4]

    node2.neighbors = [node1, node3]

    node3.neighbors = [node2, node4]

    node4.neighbors = [node1, node3]

    # Input node for your function

    input_node = node1

    # Call your solution

    cloned_graph = Solution().cloneGraph(input_node)
    print(cloned_graph)
