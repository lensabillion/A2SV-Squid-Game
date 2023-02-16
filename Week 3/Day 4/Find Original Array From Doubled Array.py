class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
       
        changed.sort()
        hash_map = {} 
        ans = []
        for i in changed:
            if i not in hash_map:
                hash_map[i] = 0
            hash_map[i] += 1
            
        for el in changed:
            
            if hash_map[el] > 0:
                
                if 2*el in hash_map and hash_map[2*el] > 0:
                    ans.append(el)
                    hash_map[el] -= 1
                    hash_map[2*el] -=1
      
        for c in hash_map:
            if hash_map[c] != 0:
                return []
        return ans
    