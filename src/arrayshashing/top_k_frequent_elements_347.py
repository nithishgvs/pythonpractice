# File: top_k_frequent_elements.py
import heapq
from typing import List


class TopKFrequentElements:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        max_heap = [(-value, key) for key, value in freq_map.items()]

        heapq.heapify(max_heap)
        result = []

        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])

        return result


def test_topk():
    list = [1, 1, 1, 2, 2, 3];
    object = TopKFrequentElements()
    print(object.topKFrequent(list, 2))
