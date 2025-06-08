class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.generate_pattern(s)== self.generate_pattern(t)

    def generate_pattern(self, s):
        dict = {}
        pattern = ""
        for index, _ in enumerate(s):
            if _ not in dict:
                dict[_] = index
            pattern += str(dict[_]) + "_"
        return pattern

