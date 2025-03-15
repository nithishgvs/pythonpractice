# File: top_k_frequent_elements.py
import heapq
from collections import Counter
from typing import List


class TopKFrequentElements:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [item for item, _ in heapq.nlargest(k, counter.items(), key=lambda x: x[1])]


def test_topk():
    list = [1, 1, 1, 2, 2, 3];
    object = TopKFrequentElements()
    print(object.topKFrequent(list, 2))
