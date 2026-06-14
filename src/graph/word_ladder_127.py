import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)
        length = 1

        if endWord not in s:
            return 0

        queue = collections.deque()
        queue.append(beginWord)
        s.discard(beginWord)

        while queue:

            for i in range(len(queue)):
                word = queue.popleft()
                char_list = list(word)

                if endWord == word:
                    return length

                for index in range(len(word)):
                    orig = char_list[index]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        char_list[index] = c
                        new_word = ''.join(char_list)
                        if new_word in s:
                            queue.append(new_word)
                            s.discard(new_word)
                    char_list[index] = orig

            length += 1

        return 0


def test_1():
    solution = Solution()
    assert solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
