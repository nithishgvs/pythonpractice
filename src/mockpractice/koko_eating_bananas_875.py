import math


class Solution:
    def can_eat(self, speed, piles):
        total = 0
        for pile in piles:
            total += math.ceil(pile / speed)
        return total

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort()
        low = 1
        high = piles[len(piles) - 1]
        min_speed = 0

        while low <= high:
            speed = (low + high) // 2
            can_speed = self.can_eat(speed, piles)
            if can_speed <= h:
                min_speed = speed
                high = speed - 1
            else:
                low = speed + 1
        return min_speed


def test():
    s = Solution()
    print(s.minEatingSpeed([30, 11, 23, 4, 20], 6))
