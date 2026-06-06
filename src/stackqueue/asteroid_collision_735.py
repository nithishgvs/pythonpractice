from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for a in asteroids:
            stack.append(a)
            while len(stack) >= 2 and stack[-2] > 0 > stack[-1]:
                first = stack.pop()
                second = stack.pop()
                if abs(first) > abs(second):
                    stack.append(first)
                elif abs(second) > abs(first):
                    stack.append(second)
        return stack


def test_asteroid():
    asteroids = [10, 2, -5]
    object = Solution()
    print(object.asteroidCollision(asteroids=asteroids))
