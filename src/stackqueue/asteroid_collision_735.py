from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) >= 2 and stack[-2] > 0 > stack[-1] < 0:
                first = stack.pop()
                second = stack.pop()
                if (abs(first) > abs(second)):
                    stack.append(first)
                elif (abs(first) < abs(second)):
                    stack.append(second)
        return stack


def test_asteroid():
    asteroids = [10,2,-5]
    object = Solution()
    print(object.asteroidCollision(asteroids=asteroids))
