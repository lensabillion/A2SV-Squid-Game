class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hash_map = defaultdict(int)
        ans = 0
        for t in time:
            r = t % 60
            if r == 0:
                ans += hash_map[r]
            else:
                ans += hash_map[60-r]
            hash_map[r] += 1
        return ans