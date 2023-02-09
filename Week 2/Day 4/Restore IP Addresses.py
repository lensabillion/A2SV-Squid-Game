class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
       
        ans = []     
        def backtrack(s, ans, k, part):
            if k==5 and len(s)==0:
                ans.append(part[:-1])
                return
            if k== 5 or len(s)==0:
                return
            
            for i in range(3):
                if k>4 or i+1>len(s):
                    break
                
                if int(s[:i+1])>255:
                    continue
                if i != 0 and s[0]=='0':
                    continue
                        
                backtrack(s[i+1:], ans, k+1, part+s[:i+1]+'.')
        backtrack(s, ans, 1, "")
        return ans