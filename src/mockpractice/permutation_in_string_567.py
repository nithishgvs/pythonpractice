from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        s2_map = {}

        left = 0
        for right in range(len(s2)):
            s2_map[s2[right]] = s2_map.get(s2[right], 0) + 1

            window_size = right - left + 1

            if window_size > len(s1):
                s2_map[s2[left]] = s2_map[s2[left]] - 1
                if s2_map[s2[left]] == 0:
                    del s2_map[s2[left]]
                left += 1

            if s2_map == s1_map:
                return True
        return False


def test():
    s = Solution()
    print(s.checkInclusion("ab", "eidboaoo"))
