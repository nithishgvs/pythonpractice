import heapq
from typing import List

# Hierholzer's algorithm: finds an Eulerian path by greedily following edges
# and appending nodes in post-order (after all their outgoing edges are exhausted).
# Reversing the post-order list gives the correct traversal order.


def dfs(result, src, itinerary):
    # Visit neighbors in lexical order (min-heap) before appending current node
    while itinerary.get(src):
        new_city = heapq.heappop(itinerary.get(src))
        dfs(result, new_city, itinerary)

    # Post-order: append only after all outgoing edges from src are visited
    result.append(src)


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary = {}

        # Build adjacency list as min-heaps to ensure lexical order of destinations
        for src, dest in tickets:
            destinations = itinerary.get(src, [])
            heapq.heappush(destinations, dest)
            itinerary[src] = destinations

        result = []

        dfs(result, "JFK", itinerary)

        # Reverse post-order result to get the correct itinerary order
        return result[::-1]


def test_itin():
    solution = Solution()
    assert solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == [
        "JFK",
        "MUC",
        "LHR",
        "SFO",
        "SJC",
    ]
    assert solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]) == [
        "JFK",
        "ATL",
        "JFK",
        "SFO",
        "ATL",
        "SFO",
    ]
