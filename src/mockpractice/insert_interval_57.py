class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        stack = []

        for i in range(len(intervals)):
            interval = intervals[i]
            if stack and interval[0] <= stack[-1][1]:
                old_interval = stack.pop()
                stack.append([min(old_interval[0], interval[0]), max(old_interval[1], interval[1])])
            else:
                stack.append(interval)
        return stack


def test():
    s = Solution()
    assert s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
        [1, 2], [3, 10], [12, 16]
    ]
