class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)
        self.times = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append(value)
        self.times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        t = self.times[key]
        l, r = 0, len(t)
        while l < r:
            idx = (l + r) // 2
            if t[idx] > timestamp:
                r = idx
            else:
                l = idx + 1
        return self.vals[key][l - 1] if l > 0 else ""
