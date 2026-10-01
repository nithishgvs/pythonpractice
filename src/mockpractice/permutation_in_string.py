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


def test():
    s = Solution()
    print(s.checkInclusion("ab", "eidboaoo"))
