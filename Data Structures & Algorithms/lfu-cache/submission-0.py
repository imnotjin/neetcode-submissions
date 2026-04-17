from collections import OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        
        val = self.key_to_val[key]
        self._increment_freq(key)
        return val
        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._increment_freq(key)
        else:
            if len(self.key_to_val) == self.cap:
                evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_val[evict_key]
                del self.key_to_freq[evict_key]
            self.key_to_val[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = None
            self.min_freq = 1
    
    def _increment_freq(self, key):
        freq = self.key_to_freq[key]
        self.key_to_freq[key] = freq + 1
        del self.freq_to_keys[freq][key]

        # bucket empty = update min_freq
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1

        self.freq_to_keys[freq + 1][key] = None
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)