from typing import List


def is_palindrome(s: str, start: int, end: int) -> bool:
    while start < end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result: List[List[str]] = []
        partition: List[str] = []

        def backtrack(start: int) -> None:
            if start == len(s):
                result.append(partition.copy())
                return

            for end in range(start, len(s)):
                # Choose only palindromic prefixes for the current partition.
                if not is_palindrome(s, start, end):
                    continue

                partition.append(s[start:end + 1])
                backtrack(end + 1)
                partition.pop()

        backtrack(0)
        return result


def test1():
    sol = Solution()
    result = sol.partition("aab")

    assert sorted(result) == sorted([["a", "a", "b"], ["aa", "b"]])


def test_single_character():
    sol = Solution()

    assert sol.partition("a") == [["a"]]


def test_all_same_characters():
    sol = Solution()
    result = sol.partition("aaa")

    assert sorted(result) == sorted(
        [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
    )
