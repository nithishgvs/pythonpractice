from collections import defaultdict
from typing import List


class GroupAnagrams:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for s in strs:
            sorted_key = ''.join(sorted(s))  # Sorting the string as a key
            anagram_dict[sorted_key].append(s)

        return list(anagram_dict.values())  # Directly return grouped anagrams


def test_greoup_anagrams():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    object = GroupAnagrams()
    print(object.groupAnagrams(strs))
