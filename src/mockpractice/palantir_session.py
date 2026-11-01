import heapq


class SessionManager:
    def __init__(self, servers: set[str]):
        self._servers = {s: set() for s in servers}
        self._session_to_server = {}
        self._min_heap = [(0, s) for s in servers]
        heapq.heapify(self._min_heap)

    def get_current_allocation(self) -> dict[str, set[str]]:
        return self._servers

    def start_session(self, session_id: str) -> None:
        if session_id in self._session_to_server or len(self._min_heap) == 0:
            return
        count, server = heapq.heappop(self._min_heap)
        self._servers[server].add(session_id)
        heapq.heappush(self._min_heap, (count + 1, server))
        self._session_to_server[session_id] = server

    def end_session(self, session_id: str) -> None:
        if session_id not in self._session_to_server:
            return
        server = self._session_to_server[session_id]
        del self._session_to_server[session_id]
        self._servers[server].remove(session_id)

        # balance the servers
        min_server = min(self._servers, key=lambda s: len(self._servers[s]))
        max_server = max(self._servers, key=lambda s: len(self._servers[s]))

        if len(self._servers[max_server]) > len(self._servers[min_server]):
            moved_session = self._servers[max_server].pop()
            self._servers[min_server].add(moved_session)
            self._session_to_server[moved_session] = min_server

        # reconstruct heap
        self._min_heap = [(len(sessions), server) for server, sessions in self._servers.items()]
        heapq.heapify(self._min_heap)


if __name__ == "__main__":
    manager = SessionManager({"server1", "server2", "server3"})
    manager.start_session("s1")
    manager.start_session("s2")
    manager.start_session("s3")
    manager.start_session("s4")
    manager.start_session("s5")
    manager.start_session("s6")
    print("Initial allocation:")
    print(manager.get_current_allocation())
    # End session s5
    manager.end_session("s5")
    print("After ending s5:")
    print(manager.get_current_allocation())
    # End session s2
    manager.end_session("s2")
    print("After ending s2:")

    print(manager.get_current_allocation())
