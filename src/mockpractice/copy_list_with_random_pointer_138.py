from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current: Node = head

        nodes = {}

        while current:
            nodes[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            nodes[current].next = nodes.get(current.next)
            nodes[current].random = nodes.get(current.random)
            current = current.next
        return nodes.get(head)


def _nodes_in_order(head):
    nodes = []
    while head:
        nodes.append(head)
        head = head.next
    return nodes


def test_copy_random_list_preserves_values_and_pointer_topology():
    first = Node(7)
    second = Node(13)
    third = Node(11)
    fourth = Node(10)
    fifth = Node(1)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    second.random = first
    third.random = fifth
    fourth.random = third
    fifth.random = first

    copied_head = Solution().copyRandomList(first)

    original_nodes = _nodes_in_order(first)
    copied_nodes = _nodes_in_order(copied_head)

    assert [node.val for node in copied_nodes] == [7, 13, 11, 10, 1]
    assert len(copied_nodes) == len(original_nodes)
    assert all(copied is not original for copied, original in zip(copied_nodes, original_nodes))

    copied_indexes = {node: index for index, node in enumerate(copied_nodes)}
    assert [copied_indexes.get(node.random) for node in copied_nodes] == [None, 0, 4, 2, 0]


def test_copy_random_list_handles_self_references_and_duplicate_values():
    first = Node(1)
    second = Node(1)
    third = Node(1)
    first.next = second
    second.next = third
    first.random = first
    second.random = third
    third.random = second

    copied_head = Solution().copyRandomList(first)
    copied_first, copied_second, copied_third = _nodes_in_order(copied_head)

    assert copied_first.random is copied_first
    assert copied_second.random is copied_third
    assert copied_third.random is copied_second
    assert copied_first is not first
    assert copied_second is not second
    assert copied_third is not third


def test_copy_random_list_does_not_share_nodes_or_mutate_original_list():
    first = Node(3)
    second = Node(3)
    first.next = second
    first.random = second
    second.random = first

    copied_head = Solution().copyRandomList(first)
    copied_head.val = 99
    copied_head.random = None

    assert first.val == 3
    assert first.next is second
    assert first.random is second
    assert second.random is first
    assert copied_head.next is not second


def test_copy_random_list_returns_none_for_an_empty_list():
    assert Solution().copyRandomList(None) is None
