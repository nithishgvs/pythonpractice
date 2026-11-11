class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, h = 0, len(s) - 1

        while l < h:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[h].isalnum():
                h -= 1
                continue

            if s[l].lower() != s[h].lower():
                return False
            h -= 1
            l += 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome('A man, a plan, a canal: Panama'))
