class Solution:

    def __init__(self, w: List[int]):        
        self.w = w
        self.c = [0] * len(w)
        total = sum(w)
        self.c[0] = w[0]/total
        for i in range(1, len(w)):
            self.c[i] = self.c[i-1] + w[i]/total
    def pickIndex(self) -> int:
        pr = random.random()
        return bisect.bisect_left(self.c, pr)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()