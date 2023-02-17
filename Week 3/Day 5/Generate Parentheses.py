class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(path, left, right):
            if left == right == n:
                result.append(path)
                return
            
            if left < n:
                dfs(path+"(", left+1, right)
            if right < left:
                dfs(path+")", left, right+1)
        
        result = []
        dfs("", 0, 0)
        
        return result