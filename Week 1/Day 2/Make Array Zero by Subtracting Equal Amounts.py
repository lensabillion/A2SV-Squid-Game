class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        cnt = 0
        copy = deque([])
        for num in nums:
            if num != 0:
                copy.append(num)
        
        while copy:
            curr_min = min(copy)
            for i in range(len(copy)):
                curr = copy.popleft()
                if (curr - curr_min ) != 0:
                    copy.append((curr - curr_min ))
            cnt += 1
        return cnt