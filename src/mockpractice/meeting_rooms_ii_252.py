import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        rooms = []

        for start, end in intervals:
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        return len(rooms)


def test():
    s = Solution()
    print(s.minMeetingRooms([[9, 10], [4, 9], [4, 17]]))
