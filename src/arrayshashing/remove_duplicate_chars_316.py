class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = []
        index_map = {}
        for idx, char in enumerate(s):
            index_map[char] = idx

        seen = set()

        for idx, char in enumerate(s):
            if char not in seen:
                while result and result[-1] > char and index_map[result[-1]] > idx:
                    seen.remove(result.pop())
                seen.add(char)
                result.append(char)

        return ''.join(result)


def test_char():
    object = Solution()
    print(object.removeDuplicateLetters("bcabc"))
