class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


def test_dup():
    obj = Solution()

    assert obj.removeDuplicates("abbaca") == "ca"
    assert obj.removeDuplicates("azxxzy") == "ay"
    assert obj.removeDuplicates("aaaaaaaa") == ""
    assert obj.removeDuplicates("aaa") == "a"
    assert obj.removeDuplicates("a") == "a"
    assert obj.removeDuplicates("ab") == "ab"
