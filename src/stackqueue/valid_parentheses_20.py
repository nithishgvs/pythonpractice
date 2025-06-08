class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {']': '[', ')': '(', '}': '{'}
        for char in s:
            if stack:
                if dict.get(char, '') == stack[0]:
                    stack.pop(0)
                else:
                    stack.insert(0, char)
            else:
                stack.insert(0, char)
        return len(stack) == 0


def test_valid_paren():
    sol = Solution()
    print(sol.isValid("([])"))
