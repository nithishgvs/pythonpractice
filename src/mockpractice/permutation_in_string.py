class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}

        for c in s1:
            s1_dict[c] = s1_dict.get(c, 0) + 1

        left = 0

        s2_dict = {}
        for right in range(len(s2)):
            c = s2[right]
            s2_dict[c] = s2_dict.get(c, 0) + 1


            if right - left + 1 > len(s1):
                left_char = s2[left]
                s2_dict[left_char] = s2_dict.get(left_char) - 1
                if s2_dict[left_char] == 0:
                    del s2_dict[left_char]
                left += 1

            if s1_dict == s2_dict:
                return True

        return False


def run_tests():
    s = Solution()
    cases = [
        # (s1, s2, expected)
        ("ab", "eidbaooo", True),   # LeetCode example 1
        ("ab", "eidboaoo", False),  # LeetCode example 2
        ("ab", "ab", True),         # permutation at start
        ("ab", "oooba", True),      # permutation at end
        ("abc", "ab", False),       # s1 longer than s2
        ("a", "a", True),
        ("a", "b", False),
        ("aa", "baa", True),        # repeated characters
        ("aab", "aaa", False),
        ("abc", "abc", True),       # identical strings
        ("ab", "aab", True),        # overlapping windows
        ("adc", "dcda", True),
    ]
    passed = 0
    for s1, s2, expected in cases:
        result = s.checkInclusion(s1, s2)
        if result == expected:
            passed += 1
        else:
            print(f"FAIL: checkInclusion({s1!r}, {s2!r}) = {result}, expected {expected}")
    print(f"{passed}/{len(cases)} tests passed")
    assert passed == len(cases), "Some tests failed"


if __name__ == "__main__":
    run_tests()
