class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        seen = set()
        ans =[]
        hash_map = defaultdict(list)
        for pair in adjacentPairs:
            hash_map[pair[0]].append(pair[1])
            hash_map[pair[1]].append(pair[0])
       
        def dfs(ind):
            ans.append(ind)
            for nxt in hash_map[ind]:
                if nxt not in seen:
                    seen.add(nxt)
                    dfs(nxt)
        for  el in hash_map:
            if len(hash_map[el]) == 1:
                seen.add(el)
                dfs(el)                
                break
        return ans