from src.linkedlist.list_node import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        fastptr: ListNode = dummy
        slowptr: ListNode = dummy

        count = 0

        while count < n:
            fastptr = fastptr.next
            count += 1

        while fastptr.next:
            fastptr = fastptr.next
            slowptr = slowptr.next

        slowptr.next = slowptr.next.next

        return dummy.next


def _linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def _values(head: ListNode | None) -> list[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def test_remove_nth_from_end_removes_a_middle_node():
    head = _linked_list([1, 2, 3, 4, 5])

    result = Solution().removeNthFromEnd(head, 2)

    assert _values(result) == [1, 2, 3, 5]


def test_remove_nth_from_end_removes_the_tail():
    head = _linked_list([1, 2, 3])

    result = Solution().removeNthFromEnd(head, 1)

    assert _values(result) == [1, 2]


def test_remove_nth_from_end_removes_the_head_when_n_equals_length():
    head = _linked_list([1, 2, 3])

    result = Solution().removeNthFromEnd(head, 3)

    assert _values(result) == [2, 3]


def test_remove_nth_from_end_removes_the_only_node():
    result = Solution().removeNthFromEnd(ListNode(1), 1)

    assert result is None
