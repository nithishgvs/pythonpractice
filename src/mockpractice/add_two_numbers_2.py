class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = 0
        dummyHead = ListNode(0)
        current = dummyHead

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            current.next = ListNode(carry % 10)
            current = current.next
            carry = carry // 10
        return dummyHead.next


def test():
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    result = Solution().addTwoNumbers(l1, l2)

    expected = [8, 9, 9, 9, 0, 0, 0, 1]
    actual = []

    while result:
        actual.append(result.val)
        result = result.next

    assert actual == expected, f"Expected {expected}, got {actual}"
    print("Test passed!")
