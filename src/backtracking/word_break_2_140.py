from typing import List, Set


class Solution:
    # Time: O(n * 2^n) - worst case (e.g. s = "aaaa", wordDict = ["a","aa","aaa","aaaa"], i.e.
    #   every prefix is a valid word) each of the n-1 gaps between characters can independently
    #   be a cut point or not, giving 2^(n-1) complete partitions (verified empirically: result
    #   count matches 2^(n-1) exactly for n up to 14). Building/joining each path's words costs
    #   O(n), giving O(n * 2^n) overall; the per-branch slicing/set-lookup work is dominated by
    #   this term.
    # Space: O(n) auxiliary (temp list + recursion depth), not counting the output which itself
    #   holds O(n * 2^n) characters across all sentences in the worst case.
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result: List[str] = []
        temp = []

        words = set(wordDict)

        def backtrack(start: int):
            if start == len(s):
                result.append(" ".join(temp))
                return

            for end in range(start, len(s)):
                sub_str = s[start:end + 1]
                if sub_str in words:
                    temp.append(sub_str)
                    backtrack(end + 1)
                    temp.pop()

        backtrack(0)
        return result


def test1():
    sol = Solution()
    print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
