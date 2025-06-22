class DoublyLinkedNode:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = None
        self.visit(homepage)

    def visit(self, url: str) -> None:
        new_node = DoublyLinkedNode(url)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            new_node.prev = curr_node
            curr_node.next = new_node
            self.head = new_node

    def back(self, steps: int) -> str:
        curr_node = self.head

        while curr_node.prev and steps > 0:
            curr_node = curr_node.prev
            steps -= 1
        self.head = curr_node
        return self.head.value

    def forward(self, steps: int) -> str:
        curr_node = self.head

        while curr_node.next and steps > 0:
            curr_node = curr_node.next
            steps -= 1
        self.head = curr_node
        return self.head.value


def test_browser():
    object = BrowserHistory('leetcode.com')
    object.visit('google.com')
    object.visit('facebook.com')
    object.visit('youtube.com')
    print(object.back(1))#returns facebook.com
    print(object.back(1))#returns google.com
    print(object.forward(1))#returns facebook.com
    object.visit('linkedin.com')
    print(object.forward(2))
    print(object.back(2))
    print(object.back(7))
