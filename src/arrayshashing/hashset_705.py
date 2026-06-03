class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[self._hash(key)]
        return key in bucket


def test_hashset():
    myHashSet = MyHashSet()
    myHashSet.add(1)
    myHashSet.add(2)
    print(myHashSet.contains(1))  # True
    print(myHashSet.contains(3))  # False
    myHashSet.add(2)
    print(myHashSet.contains(2))  # True
    myHashSet.remove(2)
    print(myHashSet.contains(2))  # False
    myHashSet.add(1000000)
    print(myHashSet.contains(1000000))  # True
