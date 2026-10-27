class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def solve(idx1: int, idx2: int, idx3: int) -> bool:
            if idx1 < 0 or idx2 < 0 or idx3 < 0:
                return False

            if idx1 + idx2 != idx3:
                return False

            if idx1 == 0 and idx2 == 0:
                return True

            if (idx1, idx2, idx3) in dp:
                return dp[(idx1, idx2, idx3)]

            take_from_s1 = (
                idx1 > 0
                and s1[idx1 - 1] == s3[idx3 - 1]
                and solve(idx1 - 1, idx2, idx3 - 1)
            )
            take_from_s2 = (
                idx2 > 0
                and s2[idx2 - 1] == s3[idx3 - 1]
                and solve(idx1, idx2 - 1, idx3 - 1)
            )

            result = take_from_s1 or take_from_s2
            dp[(idx1, idx2, idx3)] = result
            return result

        return solve(len(s1), len(s2), len(s3))


def test():
    s = Solution()
    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
    assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") is False
    assert s.isInterleave("aa", "ab", "aaba") is True
    assert s.isInterleave("ab", "ab", "abba") is False
    assert s.isInterleave("", "", "") is True
