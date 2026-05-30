import pytest
from typing import List


class TrieNode:
    def __init__(self, is_end_of_word: bool = False, children: dict = None):
        self.is_end_of_word = is_end_of_word
        self.children = children if children is not None else {}


class Trie:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()
        self.result = ""

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end_of_word = True

    def dfs(self, node: TrieNode, current_string: str) -> None:
        if len(current_string) > len(self.result) or (
            len(current_string) == len(self.result) and current_string < self.result
        ):
            self.result = current_string
        for ch, child in node.children.items():
            if child.is_end_of_word:
                self.dfs(child, current_string + ch)


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        trie.dfs(trie.root, "")
        return trie.result


@pytest.fixture
def solution():
    return Solution()


def test_basic_longest_word(solution):
    assert solution.longestWord(["a", "ap", "app", "appl", "apple"]) == "apple"


def test_lexicographic_tie(solution):
    assert solution.longestWord(["a", "b", "ba", "bca", "bcd", "bcde"]) == "ba"


def test_multiple_valid_same_length(solution):
    assert solution.longestWord(["a", "ab", "b", "bc"]) == "ab"


def test_no_valid_word(solution):
    assert solution.longestWord(["banana"]) == ""


def test_single_char_words(solution):
    assert solution.longestWord(["a", "b", "c"]) in ["a", "b", "c"]


def test_empty_input(solution):
    assert solution.longestWord([]) == ""


def test_all_prefixes_present(solution):
    assert solution.longestWord(["a", "ap", "app", "appl", "apple", "applet"]) == "applet"