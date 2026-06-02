from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()

        for i in range(len(s) - 10 + 1):
            window = s[i:i + 10]
            if window in seen:
                repeated.add(window)
            else:
                seen.add(window)
        return list(repeated)
