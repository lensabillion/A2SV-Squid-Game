class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_s_t = {}
        hash_t_s = {}
       
        for i in range(len(s)):
            
            if (s[i] not in hash_s_t) and (t[i] not in hash_t_s):
                hash_s_t[s[i]] = t[i]
                hash_t_s[t[i]] = s[i]
            elif hash_s_t.get(s[i]) != t[i] or hash_t_s.get(t[i]) != s[i]:
                return False
        return True