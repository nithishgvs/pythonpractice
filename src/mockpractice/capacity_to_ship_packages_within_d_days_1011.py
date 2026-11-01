class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l = max(weights)
        h = sum(weights)

        def canShip(mid, weights):
            curr_day = 1
            sum = 0
            for w in weights:
                sum += w
                if sum <= mid:
                    continue
                else:
                    sum = w
                    curr_day += 1
            return curr_day

        while l < h:
            mid = (l + h) // 2
            curr_days = canShip(mid, weights)
            if curr_days <= days:
                h = mid
            else:
                l = mid + 1
        return l


def test():
    s = Solution()
    print(s.shipWithinDays([1, 2, 3, 1, 1], 4))
