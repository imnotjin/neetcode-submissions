class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def get_bucket(self, key):
        return self.buckets[key % self.size]

    def add(self, key: int) -> None:
        bucket = self.get_bucket(key)
        if not self.contains(key):
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.get_bucket(key)
        if self.contains(key):
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.get_bucket(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)