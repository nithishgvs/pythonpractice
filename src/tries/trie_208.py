import pytest


class TrieNode:
    def __init__(self, is_end_of_word: bool = False, children: dict = None):
        self.is_end_of_word = is_end_of_word
        self.children = children if children is not None else {}


class Trie:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for ch in word:
            children = current.children.get(ch)
            if children is None:
                return False
            current = children
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for ch in prefix:
            children = current.children.get(ch)
            if children is None:
                return False
            current = children
        return True

# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


@pytest.fixture
def trie():
    t = Trie()
    t.insert("apple")
    t.insert("app")
    t.insert("application")
    return t


def test_search_exact_word(trie):
    assert trie.search("apple") is True


def test_search_prefix_not_word(trie):
    assert trie.search("ap") is False


def test_search_missing_word(trie):
    assert trie.search("banana") is False


def test_search_empty_string():
    t = Trie()
    t.insert("")
    assert t.search("") is True


def test_search_empty_string_not_inserted():
    t = Trie()
    assert t.search("") is False


def test_starts_with_valid_prefix(trie):
    assert trie.startsWith("app") is True


def test_starts_with_single_char(trie):
    assert trie.startsWith("a") is True


def test_starts_with_full_word(trie):
    assert trie.startsWith("apple") is True


def test_starts_with_missing_prefix(trie):
    assert trie.startsWith("ban") is False


def test_starts_with_beyond_inserted_word(trie):
    assert trie.startsWith("applez") is False


def test_insert_duplicate(trie):
    trie.insert("apple")
    assert trie.search("apple") is True


def test_insert_and_search_multiple_words(trie):
    assert trie.search("app") is True
    assert trie.search("application") is True


def test_search_substring_not_inserted():
    t = Trie()
    t.insert("hello")
    assert t.search("hell") is False
    assert t.startsWith("hell") is True