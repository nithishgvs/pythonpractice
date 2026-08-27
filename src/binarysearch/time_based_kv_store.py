from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.map = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            inner_keys = sorted(self.map[key].keys())
            l, h = 0, len(inner_keys) - 1
            while l <= h:
                mid = l + (h - l) // 2
                if timestamp > inner_keys[mid]:
                    l = mid + 1
                elif timestamp < inner_keys[mid]:
                    h = mid - 1
                else:
                    return self.map[key][inner_keys[mid]]
            return "" if h < 0 else self.map[key][inner_keys[h]]
        else:
            return ""


def test():
    timeMap = TimeMap()
    timeMap.set("love", "high", 10)
    timeMap.set("love", "low", 20)
    print(timeMap.get("love", 5))
    print(timeMap.get("love", 10))
    print(timeMap.get("love", 15))
    print(timeMap.get("love", 20))
    print(timeMap.get("love", 35))
    print("")


def test2():
    timeMap = TimeMap()
    timeMap.set("a", "bar", 1)
    timeMap.set("x", "b", 3)
    print(timeMap.get("b", 3))
    timeMap.set("foo", "bar", 4)
    print(timeMap.get("foo", 4))
    print(timeMap.get("foo", 5))
