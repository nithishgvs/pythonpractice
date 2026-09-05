from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        stack = []

        for i in range(n - 1, -1, -1):

            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i

            stack.append(i)

        return result


def test():
    s = Solution()
    s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
