from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        stack = []

        intervals.sort(key=lambda x: x[0])
        stack.append(intervals[0])

        for idx in range(1, len(intervals)):
            if stack and stack[-1][1] >= intervals[idx][0]:
                last_entry = stack.pop()
                stack.append([last_entry[0], max(last_entry[1], intervals[idx][1])])
            else:
                stack.append(intervals[idx])

        return stack


def test():
    sol = Solution()
    print(sol.merge([[4, 7], [1, 4]]))
