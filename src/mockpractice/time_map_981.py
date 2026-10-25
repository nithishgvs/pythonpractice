class TimeMap:

    def __init__(self):
        self.time_map: dict[str, list[tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        history = self.time_map.get(key, [])
        l = 0
        h = len(history) - 1

        while l <= h:
            mid = (l + h) // 2
            if history[mid][0] <= timestamp:
                result = history[mid][1]
                l = mid + 1
            else:
                h = mid - 1
        return result


def test():
    timeMap = TimeMap()
    timeMap.set("love", "high", 10)
    timeMap.set("love", "low", 20)
    assert timeMap.get("love", 5) == ""
    assert timeMap.get("love", 10) == "high"
    assert timeMap.get("love", 15) == "high"
    assert timeMap.get("love", 20) == "low"
    assert timeMap.get("love", 25) == "low"
    assert timeMap.get("missing", 10) == ""
