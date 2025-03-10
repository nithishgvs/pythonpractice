class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        dict_map = {}
        start = 0  # Left pointer

        for end in range(len(s)):  # Right pointer
            char = s[end]
            dict_map[char] = dict_map.get(char, 0) + 1

            # If a duplicate is found, shrink the window
            while dict_map[char] > 1:
                start_char = s[start]
                dict_map[start_char] -= 1
                if dict_map[start_char] == 0:
                    del dict_map[start_char]  # Safely delete the key
                start += 1  # Move left pointer

            # Update max length
            max_length = max(max_length, end - start + 1)

        return max_length


def test():
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))
