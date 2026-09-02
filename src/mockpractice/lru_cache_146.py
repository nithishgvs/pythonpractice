class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, key: int, value: int):
        # append at the head of the double linked list
        new_node = Node(key, value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            head_node = self.head
            new_node.next = head_node
            head_node.prev = new_node
            self.head = new_node
        self.size += 1
        return new_node

    def delete(self, node: Node):

        if node.prev:
            node.prev.next = node.next
        else:
            # if this node is head prev will be null
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            # this is tail node then
            self.tail = node.prev
        self.size -= 1

class LRUCache:

    def __init__(self, capacity: int):
        self.doubleLinkedList = DoubleLinkedList()
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        del self.cache[key]
        self.doubleLinkedList.delete(node)
        new_node = self.doubleLinkedList.append(node.key, node.value)
        self.cache[key] = new_node
        return new_node.value

    def put(self, key: int, value: int) -> None:
        #Key may be already present so we need to update it
        if key in self.cache:
            self.doubleLinkedList.delete(self.cache[key])
        new_node = self.doubleLinkedList.append(key, value)
        self.cache[key] = new_node
        if self.doubleLinkedList.size > self.capacity:
            # remove from tail
            tail_node = self.doubleLinkedList.tail
            self.doubleLinkedList.delete(tail_node)
            del self.cache[tail_node.key]


def test():
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # cache is {1=1}
    lRUCache.put(2, 2)  # cache is {1=1, 2=2}

    result = lRUCache.get(1)
    print(f"get(1) -> {result}")  # expected: 1
    assert result == 1

    lRUCache.put(3, 3)  # evicts key 2, cache is {1=1, 3=3}

    result = lRUCache.get(2)
    print(f"get(2) -> {result}")  # expected: -1
    assert result == -1

    lRUCache.put(4, 4)  # evicts key 1, cache is {4=4, 3=3}

    result = lRUCache.get(1)
    print(f"get(1) -> {result}")  # expected: -1
    assert result == -1

    result = lRUCache.get(3)
    print(f"get(3) -> {result}")  # expected: 3
    assert result == 3

    result = lRUCache.get(4)
    print(f"get(4) -> {result}")  # expected: 4
    assert result == 4

    print("All test cases passed!")


if __name__ == "__main__":
    test()
