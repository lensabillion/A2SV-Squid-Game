class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        carry = 0
        if len(a) < len(b):
            a = (str(0) * (len(b) -len(a))) + a
        elif len(b) < len(a):
            b = (str(0) * (len(a) -len(b))) + b
            
        for i in range(len(a)-1,-1,-1):
            if a[i] == "1" and b[i] == "1" and carry  == 0:
                ans = str(0) + ans
                carry = 1
            elif a[i] == "1" and b[i] == "1" and carry  == 1:
                ans = str(1) + ans 
                carry = 1
            elif a[i] == "1" and b[i] == "0" and carry  == 0:
                ans = str(1)  + ans
                carry = 0
            elif a[i] == "0" and b[i] == "1" and carry  == 0:
                ans = str(1)  + ans 
                carry = 0
            elif a[i] == "1" and b[i] == "0" and carry  == 1:
                ans = str(0) + ans
                carry = 1
            elif a[i] == "0" and b[i] == "1" and carry  == 1:
                ans = str(0) + ans 
                carry = 1
            elif a[i] == "0" and b[i] == "0" and carry  == 0:
                ans = str(0) + ans
                carry = 0
            elif a[i] == "0" and b[i] == "0" and carry  == 1:
                ans = str(1) + ans
                carry = 0
     
        if carry == 1:
            return str(carry)+ans
        else:
            return ans
                
            