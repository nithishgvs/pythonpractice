import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [item[0] for item in heapq.nlargest(k, Counter(nums).items(), key=lambda x: x[1])]


def test():
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
