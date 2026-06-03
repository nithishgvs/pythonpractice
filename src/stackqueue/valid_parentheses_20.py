class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pattern_map = {']': '[', ')': '(', '}': '{'}

        for ch in s:
            if len(stack) > 0 and ch in pattern_map and pattern_map[ch] == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return not stack


def test_valid_paren():
    sol = Solution()
    print(sol.isValid("([])"))
