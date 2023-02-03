class Solution:
    def simplifyPath(self, path: str) -> str:
       
        stack = []
        arr = path.split("/")
        for el in arr:
            if el == "..":
                if stack:
                    stack.pop()
            elif el == "." or el == "":
                continue
            else:
                stack.append(el)
       
        ans = "/".join(stack)
        return "/"+ans
            
  