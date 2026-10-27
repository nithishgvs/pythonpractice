from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counter_map = Counter(hand)

        for card in sorted(counter_map):
            count = counter_map[card]
            if count == 0:
                continue

            for value in range(card, card + groupSize):
                if counter_map[value] < count:
                    return False
                counter_map[value] -= count

        return True


def test1():
    s = Solution()
    assert s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True
    assert s.isNStraightHand([1, 1, 2, 2, 3, 3], 3) is True
    assert s.isNStraightHand([1, 2, 3, 4, 5], 4) is False
