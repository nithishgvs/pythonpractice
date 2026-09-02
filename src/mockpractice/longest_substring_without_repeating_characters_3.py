from src.tries.longest_word_in_dictionary_720 import solution


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_count = {}
        max_length = 0

        for end, char in enumerate(s):
            char_count[char] = char_count.get(char, 0) + 1

            while char_count[char] > 1:
                left_char = s[left]
                char_count[left_char] = char_count[left_char] - 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                left += 1
            max_length = max(max_length, end - left + 1)

        return max_length


def test():
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
