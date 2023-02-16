class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = [0] * len(nums)
        pre[0] = nums[0]
        for i in range(1, len(nums)):
            pre[i] = max(nums[i] , pre[i-1] + nums[i])
        # print(pre)
        return max(pre)