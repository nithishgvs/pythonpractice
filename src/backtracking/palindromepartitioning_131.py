from typing import List


def is_sub_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result: List[List[str]] = []
        subsets: List[str] = []

        def backtracking(start: int):

            if start == len(s):
                result.append(subsets.copy())
                return

            for end in range(start, len(s)):
                if is_sub_palindrome(s, start, end):
                    subsets.append(s[start:end + 1])
                    backtracking(end + 1)
                    subsets.pop()

        backtracking(0)
        return result


def test_1():
    sol = Solution()
    print(sol.partition("abc"))
