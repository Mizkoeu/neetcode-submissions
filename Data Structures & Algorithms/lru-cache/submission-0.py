class Node:
    def __init__(self, k, v):
        self.k, self.v = k, v
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, new_node):
        self.right.prev.next = new_node
        new_node.prev = self.right.prev
        new_node.next = self.right
        self.right.prev = new_node
    
    def make_mru(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.insert(node)

    def evict(self):
        if self.left.next.next:
            evicted = self.left.next
            self.left.next.next.prev = self.left
            self.left.next = self.left.next.next
            return evicted.k
        return -1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.make_mru(val)
        return val.v

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            val = self.cache[key]
            val.v = value
            self.make_mru(val)
        else:
            # eviction due to capacity
            if len(self.cache) >= self.cap:
                evicted = self.evict()
                del self.cache[evicted]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert(new_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)