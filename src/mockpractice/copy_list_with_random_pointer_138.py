class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copies = {}
        current = head

        while current:
            copies[current] = Node(current.val)
            current = current.next
        current = head

        while current:
            copies[current] = copies.get(current)
            copies[current].next = copies.get(current.next)
            copies[current].random = copies.get(current.random)
            current = current.next
        return copies.get(head)


def test_copy_random_list():
    first = Node(7)
    second = Node(13)
    first.next = second
    first.random = second
    second.random = first

    copied = Solution().copyRandomList(first)

    assert copied is not first
    assert copied.val == 7
    assert copied.next is not second
    assert copied.next.val == 13
    assert copied.random is copied.next
    assert copied.next.random is copied
