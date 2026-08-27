class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = float("inf")

    def push(self, value: int) -> None:
        self.current_min = min(self.current_min, value)
        self.stack.append((value, self.current_min))

    def pop(self) -> None:
        self.stack.pop()
        self.current_min = self.stack[-1][1] if self.stack else float("inf")

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def test():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)

    print(minStack.getMin());  # return -3
    print(minStack.pop())
    print(minStack.top())  # return 0
    print(minStack.getMin())
