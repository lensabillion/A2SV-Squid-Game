from collections import Counter 
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        degree = max(cnt.values())
        ans = len(nums)
        hash_map = defaultdict(int)
        j = 0
        for i in range(len(nums)):
           
            hash_map[nums[i]] += 1
           
            while len(hash_map) > 0 and j <= i and max(hash_map.values()) >=  degree:
               
                ans = min(ans, (i-j+1))
               
                hash_map[nums[j]] -= 1
                j += 1
               
            
        return ans
    