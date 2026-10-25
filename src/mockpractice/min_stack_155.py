class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        current_min = value
        if self.stack:
            current_min = min(value, self.stack[-1][1])
        self.stack.append((value, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


def test():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2
