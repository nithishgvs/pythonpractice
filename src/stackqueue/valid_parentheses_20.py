class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pattern_map = {']': '[', ')': '(', '}': '{'}
        for char in s:
            if (stack and char in pattern_map and pattern_map[char] == stack[-1]):
                stack.pop()
            else:
                stack.append(char)
        return not stack


def test_valid_paren():
    sol = Solution()
    print(sol.isValid("([])"))
