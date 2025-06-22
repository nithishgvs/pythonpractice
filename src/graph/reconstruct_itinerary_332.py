import heapq
from typing import List


def dfs(current_city, result, itin_map):

    while current_city in itin_map and itin_map[current_city]:
        dest_list = itin_map[current_city]
        new_city = heapq.heappop(dest_list)
        dfs(new_city, result, itin_map)
    result.append(current_city)

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itin_map = {}

        for ticket in tickets:
            list_current = itin_map.get(ticket[0], [])
            heapq.heappush(list_current, ticket[1])
            itin_map[ticket[0]] = list_current

        result = []

        dfs("JFK", result, itin_map)

        return result[::-1]


def test_itin():
    object = Solution()
    print(object.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
    # print(object.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
