from collections import defaultdict
from typing import Tuple, List


from collections import defaultdict
from typing import Tuple, List

class document_search:

    def __init__(self, documents: List[Tuple[int, str]]):
        self.word_to_docs = defaultdict(list)           # word -> list of doc_ids
        self.doc_id_to_words = defaultdict(list)        # doc_id -> list of words
        self.doc_preparation(documents)

    def doc_preparation(self, documents: List[Tuple[int, str]]):
        for doc_id, text in documents:
            words = text.lower().split()
            self.doc_id_to_words[doc_id] = words
            seen = set()
            for word in words:
                if word not in seen:  # avoid duplicate doc_ids for the same word
                    self.word_to_docs[word].append(doc_id)
                    seen.add(word)

    def search_word(self, word: str) -> List[int]:
        return self.word_to_docs[word.lower()]

    def search_sentence(self, phrase: str) -> List[int]:
        phrase_words = phrase.lower().split()
        result = []

        for doc_id, words in self.doc_id_to_words.items():
            for i in range(len(words) - len(phrase_words) + 1):
                if words[i:i + len(phrase_words)] == phrase_words:
                    result.append(doc_id)
                    break

        return result


def test_doc():
    documents = [
        (1, "chatgpt is powerful and helpful"),
        (2, "openai developed chatgpt using large language models"),
        (3, "language models understand context and generate responses"),
        (4, "chatgpt can answer coding and math questions"),
        (5, "is chatgpt good"),
    ]
    search_engine = document_search(documents=documents)
    print(search_engine.search_word("chatgpt"))
    print(search_engine.search_sentence("chatgpt can"))
