class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = nums
        hash_map = {}
        hash_map[0] = 1
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        for i in prefix:
            mod = i % k
            if mod in hash_map:                
                res += hash_map[mod]
                hash_map[mod] += 1
            else:
                hash_map[mod] = 1
        return res