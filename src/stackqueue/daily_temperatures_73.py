from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n

        for index in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[index]:
                stack.pop()

            if stack:
                result[index] = stack[-1] - index
            stack.append(index)
        return result


def test_temp():
    object = Solution()
    print(object.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
