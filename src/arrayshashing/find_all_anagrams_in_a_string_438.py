from collections import Counter, defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = 0

        begin = 0

        p_map = Counter(p)
        s_map = defaultdict(int)
        results = []

        while start < len(s):

            start_char = s[start]
            s_map[start_char] = s_map[start_char] + 1

            if start - begin + 1 == len(p):

                if s_map == p_map:
                    results.append(begin)

                begin_char = s[begin]

                if s_map[begin_char] > 1:
                    s_map[begin_char] = s_map[begin_char] - 1
                else:
                    del s_map[begin_char]
                begin = begin + 1


            start = start + 1

        return results


def test_1():
    object = Solution()
    print(object.findAnagrams("abab", "ab"))
