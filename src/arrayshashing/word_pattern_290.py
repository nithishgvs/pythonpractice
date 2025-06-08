class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return self.generate_pattern(pattern) == self.generate_pattern(s.split(" "))

    def generate_pattern(self, pattern):
        dict = {}
        output = ""
        for index, _ in enumerate(pattern):
            if _ not in dict:
                dict[_] = index
            output += str(dict[_])+"_"
        return output


def test_pattern():
    sol = Solution();
    print(sol.wordPattern("abba", "dog cat cat dog"))
