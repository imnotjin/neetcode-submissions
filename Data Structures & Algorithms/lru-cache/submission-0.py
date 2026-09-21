class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # key: node
        self.hashmap = {}
        # head -> LRU
        self.head = Node()
        # MRU <- tail
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.cap = capacity

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_node(self, node):
        mru = self.tail.prev
        mru.next = node
        node.prev = mru
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.remove_node(node)
        self.add_node(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove_node(node)
        else:
            node = Node(key, value)
            self.hashmap[key] = node

        self.add_node(node)

        if len(self.hashmap) > self.cap:
            lru = self.head.next
            self.remove_node(lru)
            del self.hashmap[lru.key]
