from typing import Tuple


class Solution:

    def songs(self, inputs: Tuple, target: str) -> Tuple:
        sec_target = self.convert_to_secs(target)
        map = {}
        for name, duration in inputs:
            secs = self.convert_to_secs(duration)
            if (sec_target - secs) in map:
                return map[sec_target - secs], name
            else:
                map[secs] = name

    def convert_to_secs(self, target):
        split = target.split(":")
        sec_target = int(split[0]) * 60 + int(split[1])
        return sec_target


def test():
    object = Solution()
    songs = [
        ("song_name_1", "2:30"),
        ("song_name_2", "2:45"),
        ("song_name_3", "4:30"),
        ("song_name_4", "4:15"),
    ]
    print(object.songs(songs, "7:00"))
