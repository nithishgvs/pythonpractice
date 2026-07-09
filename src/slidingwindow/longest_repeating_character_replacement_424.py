from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        left = 0
        counts = defaultdict(int)
        # max_freq is never decremented when shrinking the window — intentional:
        # the window only grows when a strictly better max_freq is found, so the
        # answer is still correct without recomputing on each shrink.
        max_freq = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            max_freq = max(max_freq, counts[s[right]])

            window_size = right - left + 1

            if window_size - max_freq <= k:
                max_length = max(max_length, window_size)
            else:
                counts[s[left]] -= 1
                left += 1

        return max_length


def test1():
    sol = Solution()
    assert sol.characterReplacement("ABCC", 1) == 3

def test_no_replacements():
    sol = Solution()
    assert sol.characterReplacement("AABABBA", 0) == 2

def test_all_same():
    sol = Solution()
    assert sol.characterReplacement("AAAA", 2) == 4

def test_k_exceeds_length():
    sol = Solution()
    assert sol.characterReplacement("ABCD", 10) == 4
