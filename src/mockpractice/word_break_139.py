from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}

        word_set = set(wordDict)
        n = len(s)

        def can_break(i: int):

            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            result = False

            for j in range(i + 1, n + 1):
                if s[i:j] in word_set and can_break(j):
                    result = True
                    break

            memo[i] = result
            return result

        return can_break(0)


def test():
    s = Solution()
    print(s.wordBreak("aaab", ["a", "aa", "aaa"]))
