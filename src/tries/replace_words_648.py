from typing import List


class TrieNode:
    def __init__(self, is_end_of_word: bool = False, children: dict = None):
        self.is_end_of_word = is_end_of_word
        self.children = children if children is not None else {}


class Trie:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end_of_word = True

    def search(self, word: str):
        current = self.root
        result = ""
        for ch in word:
            if ch not in current.children:
                return None

            children = current.children[ch]

            result += ch
            current = children
            if current.is_end_of_word:
                return result


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        result = ""

        parts = sentence.split(" ")
        for p in parts:
            partial = trie.search(p)
            result += partial if partial is not None else p
            result += " "

        return result.strip()


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_basic_replace(solution):
    assert solution.replaceWords(
        ["cat", "bat", "rat"],
        "the cattle was rattled by the battery"
    ) == "the cat was rat by the bat"


def test_no_match(solution):
    assert solution.replaceWords(["cat"], "the dog ran") == "the dog ran"


def test_exact_word_match(solution):
    assert solution.replaceWords(["cat"], "cat") == "cat"


def test_shorter_root_wins(solution):
    assert solution.replaceWords(["c", "cat"], "cattle") == "c"


def test_multiple_roots_same_word(solution):
    assert solution.replaceWords(["a", "aa", "aaa"], "aaaa") == "a"


def test_empty_dictionary(solution):
    assert solution.replaceWords([], "hello world") == "hello world"
