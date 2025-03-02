
class ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_counter = {}

        for c in s:
            chars_counter[c] = chars_counter.get(c, 0) + 1
        for c in t:
            if c not in chars_counter:
                return False
            chars_counter[c] -= 1
            if chars_counter[c] == 0:
                del chars_counter[c]

        return len(chars_counter) == 0


def test_valid_anagram():
    anagram_checker = ValidAnagram()
    assert (anagram_checker.isAnagram("ram", "mar")) is True
