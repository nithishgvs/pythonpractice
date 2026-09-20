from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        min_length = float("inf")
        left = 0
        t_map = Counter(t)
        need = len(t_map)
        have = 0
        s_map = {}

        for right in range(len(s)):
            c = s[right]
            s_map[c] = s_map.get(c, 0) + 1

            if c in t_map and s_map[c] == t_map[c]:
                have += 1

            while have == need:
                if right - left + 1 < min_length:
                    result = s[left:right + 1]
                    min_length = len(result)

                remove_char = s[left]

                s_map[remove_char] = s_map[remove_char] - 1

                if remove_char in t_map and s_map[remove_char] < t_map[remove_char]:
                    have -= 1
                left += 1

        return result


def test():
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
