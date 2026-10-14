class TrieNode:

    def __init__(self):
        self.end_of_word = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children[ch] = node
            current = node

        current.end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node is None:
                return False
            current = node
        return current.end_of_word

    def startsWith(self, prefix: str) -> bool:

        current = self.root
        for p in prefix:
            node = current.children.get(p)
            if node is None:
                return False
            current = node

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


def test():
    trie = Trie()
    trie.insert("apple")

    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    assert trie.startsWith("apl") is False
