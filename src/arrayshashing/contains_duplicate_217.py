from typing import List


class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            if (s.__contains__(num)):
                return True
            s.add(num)

        return False


def test_dup():
    object = ContainsDuplicate()
    print(object.containsDuplicate([1, 2, 3, 1]))
