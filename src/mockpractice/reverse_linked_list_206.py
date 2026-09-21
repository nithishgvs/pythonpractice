from src.linkedlist.list_node import ListNode


class Solution:
    """Reverse a singly linked list in place."""

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """Return ``head`` with its links reversed in O(n) time and O(1) space."""
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous


def test_reverse_list_reverses_nodes_in_place() -> None:
    nodes = [ListNode(value) for value in range(1, 6)]
    for current, next_node in zip(nodes, nodes[1:]):
        current.next = next_node

    reversed_head = Solution().reverseList(nodes[0])

    values = []
    current = reversed_head
    while current is not None:
        values.append(current.val)
        current = current.next

    assert values == [5, 4, 3, 2, 1]
    assert reversed_head is nodes[-1]
    assert nodes[0].next is None


def test_reverse_list_handles_empty_list() -> None:
    assert Solution().reverseList(None) is None
