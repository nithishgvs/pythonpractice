import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        min_heap = []
        for list in lists:
            current = list
            while current:
                min_heap.append(current.val)
                current = current.next
        dummy = ListNode(-1)
        current = dummy
        heapq.heapify(min_heap)

        while min_heap:
            value = heapq.heappop(min_heap)
            current.next = ListNode(value)
            current = current.next
        return dummy.next


# ---- helpers to build linked lists from plain lists and back ----
def build_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def run_tests():
    cases = [
        # (input lists, expected merged list)
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),  # LeetCode example
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([[5, 10], [1, 9], [3]], [1, 3, 5, 9, 10]),
        ([], []),  # no lists at all
        ([[]], []),  # one empty list
        ([[], [], []], []),  # all lists empty
        ([[], [1], []], [1]),  # empties mixed with a list
        ([[1, 2, 3]], [1, 2, 3]),  # single list
        ([[1, 1], [1, 1]], [1, 1, 1, 1]),  # duplicates (heap tie-break test)
        ([[-2, 0, 3], [-5, -1]], [-5, -2, -1, 0, 3]),  # negatives
        ([[1, 10], [2], [3, 4, 5, 6]], [1, 2, 3, 4, 5, 6, 10]),  # unequal lengths
        ([[2], [1]], [1, 2]),
    ]
    for i, (lists, expected) in enumerate(cases, 1):
        heads = [build_list(values) for values in lists]
        got = to_list(Solution().mergeKLists(heads))
        status = "PASS" if got == expected else "FAIL"
        print(f"Test {i}: {status}  input={lists}  expected={expected}  got={got}")


if __name__ == "__main__":
    run_tests()
