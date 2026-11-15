class TrieNode:
    def __init__(self):
        self.is_end_of_word = False
        self.children = {}


class WordDictionary:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for c in word:
            trie_node = current.children.get(c)
            if trie_node is None:
                trie_node = TrieNode()
                current.children[c] = trie_node
            current = trie_node
        current.is_end_of_word = True

    def search(self, word: str) -> bool:

        def dfs(i: int, current: TrieNode) -> bool:
            if i == len(word):
                return current.is_end_of_word
            ch = word[i]
            if ch == ".":
                for child in current.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                child = current.children.get(ch)
                if child is None:
                    return False

                return dfs(i + 1, child)

        return dfs(0, self.root)


def test():
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    obj.addWord("pad")
    obj.search(".ad")
