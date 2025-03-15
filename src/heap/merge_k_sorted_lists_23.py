import heapq
from typing import List, Optional

from src.linkedlist.list_node import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []
        index = 0

        for inner_list in lists:
            current = inner_list
            while current:
                heapq.heappush(min_heap, (current.val, index, current))
                index += 1
                current = current.next

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, _, curr_node = heapq.heappop(min_heap)
            current.next = curr_node
            current = current.next

        return dummy.next


def array_to_list(arr):
    """ Helper function to convert array to LinkedList """
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next
    return head


def test_merge_k_sorted_lists():
    merge_k = Solution()

    # Test Case 1: Merging three sorted lists
    list1 = array_to_list([1, 4, 5])
    list2 = array_to_list([1, 3, 4])
    list3 = array_to_list([2, 6])
    lists = [list1, list2, list3]

    merged_head = merge_k.mergeKLists(lists)
    print(merged_head)
