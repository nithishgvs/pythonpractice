from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def build(vals, pos):
        if not vals:
            return None
        nodes = [ListNode(v) for v in vals]
        for a, b in zip(nodes, nodes[1:]):
            a.next = b
        if pos != -1:
            nodes[-1].next = nodes[pos]
        return nodes[0]



class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def build(vals, pos):
        if not vals:
            return None
        nodes = [ListNode(v) for v in vals]
        for a, b in zip(nodes, nodes[1:]):
            a.next = b
        if pos != -1:
            nodes[-1].next = nodes[pos]
        return nodes[0]


def test():
    s = Solution()
    assert s.hasCycle(ListNode.build([3, 2, 0, -4], 1)) is True
    assert s.hasCycle(ListNode.build([1, 2], -1)) is False
    assert s.hasCycle(None) is False

