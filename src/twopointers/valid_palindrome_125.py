import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s.lower())

        l, h = 0, len(s) - 1

        while l < h:
            if s[l] != s[h]:
                return False
            l += 1
            h -= 1

        return True


def test():
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
