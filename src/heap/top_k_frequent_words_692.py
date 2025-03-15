import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        sorted_keys = sorted(counter.keys(), key=lambda word: (-counter[word], word))
        return sorted_keys[:k]


def test_topk():
    solution = Solution()
    print(solution.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
