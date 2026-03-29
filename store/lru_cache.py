class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key not in self.cache:
            print(f"❌ CACHE MISS: {key}")
            return None

        print(f"🔥 CACHE HIT: {key}")
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            print(f"♻️ UPDATE CACHE: {key}")
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        print(f"📦 INSERT INTO CACHE: {key}")

        if len(self.cache) > self.capacity:
            lru = self.head.next
            print(f"🗑️ REMOVE LRU CACHE: {lru.key}")
            self.remove(lru)
            del self.cache[lru.key]
            
lru_cache = LRUCache(capacity=3)