from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        # sort always sorts the first element i.e position but [::-1] reverses the order
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)

            if (len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)


def test_car():
    object = Solution()
    print(object.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
