from src.linkedlist.list_node import ListNode


class Solution:

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous

    def reorderList(self, head: ListNode | None) -> None:
        """
        Find the middle , reverse the second half and alternatively pick the list (claude)
        """
        if head is None or head.next is None:
            return

        slow_ptr = head
        fast_ptr = head

        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        reversed_half = self.reverseList(slow_ptr.next)
        slow_ptr.next = None

        first = head
        second = reversed_half
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


def test1():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    object = Solution()
    object.reorderList(node1)
