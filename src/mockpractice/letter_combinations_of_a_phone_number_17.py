class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result: list[str] = []

        combo = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                 "6": "mno", "7": "pqrs", "8": "tuv",
                 "9": "wxyz"}

        def dfs(index: int, curr_string: []):
            if index == len(digits):
                result.append("".join(curr_string))
                return

            chars = combo.get(digits[index])

            for ch in chars:
                curr_string.append(ch)
                dfs(index + 1, curr_string)
                curr_string.pop()

        dfs(0, [])
        return result


def test():
    s = Solution()
    print(s.letterCombinations("23"))
