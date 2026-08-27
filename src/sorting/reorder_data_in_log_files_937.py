from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            identifier, content = log.split(" ", 1)
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs.sort(key=lambda log: (
            log.split(" ", 1)[1],  # content
            log.split(" ", 1)[0]))  # identifier
        return letter_logs + digit_logs


def test1():
    sol = Solution()
    sol.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
