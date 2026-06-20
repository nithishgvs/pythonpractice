import heapq
from typing import Optional, List

from src.linkedlist.list_node import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        minheap: List[ListNode] = []
        idx = 0

        for l in lists:
            current = l
            while current:
                heapq.heappush(minheap, (current.val, idx, current))
                idx += 1
                current = current.next

        dummy = ListNode(0)
        current = dummy

        while minheap:
            val, _, curr_node = heapq.heappop(minheap)
            current.next = curr_node
            current = current.next

        return dummy.next


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    current = head

    while current:
        values.append(current.val)
        current = current.next

    return values


def test_merge_three_sorted_lists():
    solution = Solution()
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6]),
    ]

    result = solution.mergeKLists(lists)

    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_merge_empty_input():
    solution = Solution()

    assert solution.mergeKLists([]) is None


def test_merge_only_empty_lists():
    solution = Solution()

    assert solution.mergeKLists([None, None]) is None


def test_merge_mixed_empty_and_non_empty_lists():
    solution = Solution()
    lists = [
        None,
        build_linked_list([0, 2]),
        None,
        build_linked_list([1, 3]),
    ]

    result = solution.mergeKLists(lists)

    assert linked_list_to_list(result) == [0, 1, 2, 3]


def test_merge_lists_with_negative_values_and_duplicates():
    solution = Solution()
    lists = [
        build_linked_list([-10, -3, 0]),
        build_linked_list([-5, -3, 2]),
        build_linked_list([-5, 4]),
    ]

    result = solution.mergeKLists(lists)

    assert linked_list_to_list(result) == [-10, -5, -5, -3, -3, 0, 2, 4]
