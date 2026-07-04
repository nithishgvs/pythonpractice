from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque()
        queue.extend(rooms[0])
        visited.add(0)

        while queue:
            current_key = queue.popleft()
            if visited.__contains__(current_key):
                continue

            visited.add(current_key)

            queue.extend(rooms[current_key])

        return len(visited) == len(rooms)


def test_rooms():
    object = Solution()
    print(object.canVisitAllRooms([[1], [2], [3], []]))
