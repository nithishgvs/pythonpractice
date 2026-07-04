from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracking(curr_string, open_count, close_count):
            if len(curr_string) == 2 * n:
                result.append(curr_string)
                return

            if open_count < n:
                backtracking(curr_string + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtracking(curr_string + ")", open_count, close_count + 1)

        backtracking("", 0, 0)

        return result


def test_main():
    sol = Solution()
    print(sol.generateParenthesis(2))
