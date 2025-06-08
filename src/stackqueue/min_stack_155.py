class MinStack:
    stack = []

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            top_value = self.stack[0]
            self.stack.insert(0, (val, min(top_value[1], val)))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop(0)

    def top(self) -> int:
        if self.stack:
            return self.stack[0][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[0][1]


def test_min_stack():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
