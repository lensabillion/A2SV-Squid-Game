import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        n = set(nums)
        h = []
        for i in n:
            h.append(i)
        heapq.heapify(h)
        if len(h) >= 3:
            return heapq.nlargest(3,h)[-1]
        else:
            if len(h) == 1:
                return h[-1]
            if len(h) == 2 :
                if h[0] > h[1]:
                    return h[0]
                else:
                    return h[-1]