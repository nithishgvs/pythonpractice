from random import random


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.arr.append(val)
            self.dict[val] = len(self.arr)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in  self.dict:
            return False
        # move array last element to the index from where we will delete
        idx = self.dict[val]
        #last element
        last_elem = self.arr[- 1]
        self.arr[idx] = last_elem
        self.dict[last_elem] = idx
        del self.dict[val]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.arr) - 1)
        return self.arr[idx]
