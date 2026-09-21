class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        count = {}
        max_freq = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            window_length = right - left + 1

            # max_freq is monotonic (never decreased on shrink).
            # Safe: result only grows when a new max_freq is found.
            while window_length - max_freq > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
                window_length -= 1
            result = max(result, window_length)

        return result

def test():
    s = Solution()
    assert s.characterReplacement("AABABBA", 1) == 4
    assert s.characterReplacement("ABAB", 2) == 4
    assert s.characterReplacement("AAAA", 0) == 4
    assert s.characterReplacement("", 1) == 0
