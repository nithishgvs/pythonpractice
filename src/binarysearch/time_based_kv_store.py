from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""

        value_tuples = self.dict[key]

        l, h = 0, len(value_tuples) - 1

        best_match = ""

        while l <= h:
            mid = l + (h - l) // 2
            if value_tuples[mid][0] <= timestamp:
                best_match = value_tuples[mid][1]
                l = mid + 1
            else:
                h = mid - 1

        return best_match


def test_time_map():
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)  # store the key "foo" and value "bar" along with timestamp = 1.
    print(timeMap.get("foo", 1))  # return "bar"
    print(timeMap.get("foo",
                      3))  # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    timeMap.set("foo", "bar2", 4)  # store the key "foo" and value "bar2" along with timestamp = 4.
    print(timeMap.get("foo", 4))  # return "bar2"
    print(timeMap.get("foo", 5))  # return "bar2
