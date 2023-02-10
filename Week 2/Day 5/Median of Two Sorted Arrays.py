class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        ans = []
        i = len(nums1) - 1
        j = len(nums2) - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                ans.append(nums1[i])
                i -= 1
            else:
                ans.append(nums2[j])
                j -= 1

        while i >= 0:
            ans.append(nums1[i])
            i -= 1
        while j >= 0:
            ans.append(nums2[j])
            j -= 1
      
        ind = len(ans) // 2
        if len(ans) % 2 == 0:            
           return  (ans[ind-1] + ans[ind]) / 2
        else:
            return ans[ind]