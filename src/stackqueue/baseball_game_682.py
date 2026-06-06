from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)


def test_1():
    obj = Solution()

    assert obj.calPoints(["5", "2", "C", "D", "+"]) == 30
    assert obj.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
    assert obj.calPoints(["1", "C"]) == 0
    assert obj.calPoints(["10", "-5", "D", "+"]) == -20
