import heapq
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [item[0] for item in heapq.nlargest(k, counter.items(), key=lambda x: x[1])]
