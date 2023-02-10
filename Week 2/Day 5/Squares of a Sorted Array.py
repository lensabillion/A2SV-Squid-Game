class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i]** 2 > nums[j] ** 2:
                ans.append(nums[i]**2)
                i += 1
            else:
                ans.append(nums[j]**2)
                j -= 1
        return ans[::-1]