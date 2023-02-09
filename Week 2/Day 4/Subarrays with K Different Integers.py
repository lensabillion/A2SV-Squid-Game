class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMostK(nums, k):
            hash_map = defaultdict(int)
            i = 0
            res = 0
            for j in range(len(nums)):          
                hash_map[nums[j]] += 1
                while len(hash_map) > k:                  
                    hash_map[nums[i]] -= 1
                    if hash_map[nums[i]] == 0:
                        del hash_map[nums[i]]                       
                    i += 1            
              
                res += j - i + 1
            
            return res
             
        return atMostK(nums, k)-  atMostK(nums, k - 1)