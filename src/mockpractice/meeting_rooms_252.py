class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort()
        stack = []

        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if stack and stack[-1][1] > start:
                return False
            else:
                stack.append((start, end))
        return True


def test1():
    s = Solution()
    print(s.canAttendMeetings([[2,7]]))
