from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if (token == '+'):
                stack.append(stack.pop() + stack.pop())
            elif (token == '-'):
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif (token == '*'):
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif (token == '/'):
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(token))

        return stack.pop()


def test_eval():
    object = Solution()
    print(object.evalRPN(["2", "1", "+", "3", "*"]))
