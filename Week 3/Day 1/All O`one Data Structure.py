import heapq
class AllOne:

    def __init__(self):
        self.hash_map = {}
        self.maxHeap = []
        self.minHeap = []

    def inc(self, key: str) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = 0
        self.hash_map[key] += 1
    
        heapq.heappush(self.maxHeap,(-self.hash_map[key], key))
        heapq.heappush(self.minHeap,(self.hash_map[key], key))

    def dec(self, key: str) -> None:
        self.hash_map[key] -= 1
    
        heapq.heappush(self.maxHeap,(-self.hash_map[key], key))
        heapq.heappush(self.minHeap,(self.hash_map[key], key))

    def getMaxKey(self) -> str:
        
        while self.maxHeap:
            key = self.maxHeap[0][1]
           
            if -1 * self.maxHeap[0][0] == self.hash_map[key] and self.hash_map[key]:
                return key
                break
            else:
                heapq.heappop(self.maxHeap)
        return ""

    def getMinKey(self) -> str:
        
        while self.minHeap:
            key = self.minHeap[0][1]
            
            if self.minHeap[0][0] == self.hash_map[key] and self.hash_map[key]:
                return key
                break
            else:
                heapq.heappop(self.minHeap)
        return ""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()