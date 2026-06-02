class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        current_direction = "N"
        current = [0, 0]

        for i in range(4):
            for ch in instructions:
                if current_direction == "N":
                    if ch == "G":
                        current[1] += 1
                    elif ch == "L":
                        current_direction = "W"
                    elif ch == "R":
                        current_direction = "E"
                elif current_direction == "E":
                    if ch == "G":
                        current[0] += 1
                    elif ch == "L":
                        current_direction = "N"
                    elif ch == "R":
                        current_direction = "S"

                elif current_direction == "W":
                    if ch == "G":
                        current[0] -= 1
                    elif ch == "L":
                        current_direction = "S"
                    elif ch == "R":
                        current_direction = "N"
                elif current_direction == "S":
                    if ch == "G":
                        current[1] -= 1
                    elif ch == "L":
                        current_direction = "E"
                    elif ch == "R":
                        current_direction = "W"
        return current[0] == 0 and current[1] == 0


def test1():
    obj = Solution()
    print(obj.isRobotBounded("GL"))
