from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0
        q = deque([])
        for i, val in enumerate(tickets):
            q.append((i, val))
        while q:
           
            for _ in range(len(q)):
                
                ind, curr = q.popleft() 
                if ind == k and curr == 1 :
                   
                    return cnt + 1
                if (curr -1) > 0:
                    q.append((ind, curr- 1))
                    
                
                cnt += 1
        return cnt 