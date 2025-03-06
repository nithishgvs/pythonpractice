import re


class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start <= end:
            # Skip non-alphanumeric characters
            while start <= end and not s[start].isalnum():
                start += 1
            while start <= end and not s[end].isalnum():
                end -= 1

            # Compare characters (case-insensitive)
            if start <= end and s[start].lower() != s[end].lower():
                return False

            # Move pointers inward
            start += 1
            end -= 1

        return


def test_palindrome():
    object = ValidPalindrome()
    print(object.isPalindrome("Was it a car or a cat I saw?"))
