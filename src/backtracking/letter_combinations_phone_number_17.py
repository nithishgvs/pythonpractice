from typing import List


class Solution:
    # Let n = len(digits).
    # Time:  O(4^n * n) - up to 4 letters per digit gives up to 4^n
    #        combinations, each costing O(n) to join into a string.
    # Space: O(n) for the recursion stack and curr_list (excluding the output).
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        m = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        result: List[str] = []

        def backtracking(curr_index: int, curr_list: List[str]):

            if curr_index == len(digits):
                result.append("".join(curr_list))
                return

            letters = m[int(digits[curr_index])]
            for letter in letters:
                curr_list.append(letter)
                backtracking(curr_index + 1, curr_list)
                curr_list.pop()

        backtracking(0, [])
        return result


def test_1():
    solution = Solution()
    result = solution.letterCombinations("23")

    assert sorted(result) == sorted(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )


def test_2():
    solution = Solution()

    assert solution.letterCombinations("") == []


def test_3():
    solution = Solution()

    assert sorted(solution.letterCombinations("2")) == sorted(["a", "b", "c"])
