from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        combined = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos, speed in combined:
            reaching_time = (target - pos) / speed

            if not stack or reaching_time > stack[-1]:
                stack.append(reaching_time)
        return len(stack)


def test1():
    obj = Solution()
    print(obj.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
