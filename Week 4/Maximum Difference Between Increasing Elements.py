class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = float('-inf')
        minim = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = nums[i] - minim
            if nums[i] < minim:
                minim = nums[i]

        ans = max(dp)
        if ans <= 0:
            return -1
        else:
            return ans
        