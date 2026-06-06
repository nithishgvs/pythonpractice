class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node: Optional['Node']) -> Node:
            if node is None:
                return node

            if node.val in visited:
                return visited[node.val]

            root = Node(node.val)
            visited[node.val] = root

            for neigh in node.neighbors:
                root.neighbors.append(dfs(neigh))

            return root

        return dfs(node)


def test_graph():
    # Create nodes

    node1 = Node(1)

    node2 = Node(2)

    node3 = Node(3)

    node4 = Node(4)

    # Build graph:

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
