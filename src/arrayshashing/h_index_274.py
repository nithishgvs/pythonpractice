from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        h_index = 0
        h = len(citations)

        for i in range(h - 1, - 1, -1):
            papers = h - i

            if citations[i] >= papers:
                h_index = papers
            else:
                break
        return h_index


def test_hindex():
    sol = Solution()

    cases = [
        ([3, 0, 6, 1, 5], 3),  # standard example
        ([1, 3, 1], 1),         # not all papers qualify
        ([0], 0),               # no citations
        ([100], 1),             # one paper with many citations
        ([0, 0, 0], 0),         # all zeros
    ]

    for citations, expected in cases:
        result = sol.hIndex(citations)
        print(f"hIndex({citations}) = {result} (expected {expected}) -> {'PASS' if result == expected else 'FAIL'}")


if __name__ == "__main__":
    test_hindex()
