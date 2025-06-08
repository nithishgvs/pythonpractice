from collections import Counter


def is_subset(s_dict, t_dict) -> bool:
    for key, value in t_dict.items():
        if (key not in s_dict or s_dict[key] != value):
            return False
    return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        t_dict = Counter(t)

        required = len(t_dict)
        left = 0
        formed = 0

        s_dict = {}

        answer = float("inf"), 0, 0

        for right, char in enumerate(s):
            s_dict[char] = s_dict.get(char, 0) + 1

            if char in t_dict and s_dict[char] == t_dict[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < answer[0]:
                    answer = right - left + 1, left, right

                left_char = s[left]
                s_dict[left_char] = s_dict.get(left_char) - 1

                if left_char in t_dict and s_dict[left_char] < t_dict[left_char]:
                    formed -= 1

                left += 1

        return "" if answer[0] == float("inf") else s[answer[1]:answer[2] + 1]


def test1():
    object = Solution()
    print(object.minWindow("aa", "aa"))
