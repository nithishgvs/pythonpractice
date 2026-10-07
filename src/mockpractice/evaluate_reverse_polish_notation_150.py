class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    # int() truncates toward zero, as the problem requires
                    stack.append(int(a / b))
            else:
                stack.append(int(t))
        return stack[0]


def test():
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "3", "*"]))  # 9
    print(s.evalRPN(["4", "13", "5", "/", "+"]))  # 6
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
