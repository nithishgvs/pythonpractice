from typing import Optional

from src.linkedlist.list_node import ListNode


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head

        dummy = ListNode(0, head)

        previous = head
        current = head.next

        while current:

            if current.val >= previous.val:
                previous = current
                current = current.next
                continue

            temp = dummy

            while temp.next and current.val > temp.next.val:
                temp = temp.next

            previous.next = current.next
            current.next = temp.next
            temp.next = current
            current = previous.next

        return dummy.next


def test_linked():
    node1 = ListNode(5)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    object = Solution()

    object.insertionSortList(node1)
