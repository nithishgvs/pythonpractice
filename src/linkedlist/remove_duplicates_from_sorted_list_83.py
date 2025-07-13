from typing import Optional

from src.linkedlist.list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        current, prev = head.next, head

        while current:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return head


def test_linked():
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    object = Solution()

    object.deleteDuplicates(node1)
