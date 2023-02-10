class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        # hash_map = {}
        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    con = nums[i] + nums[j]
                    if con == target:
                        ans += 1
        return ans