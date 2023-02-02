class Solution:
    def numberOfWays(self, s: str) -> int:
        zero = []
        one = [0] * len(s)
        ways = 0
        for i in s:
            zero.append(int(i)) 
                   
        for i in range(1, len(zero)):
            zero[i] += zero[i-1]
        if s[0] == "0":
            one[0] = 1
            
        for i in range(1,len(s)):
            if s[i] == "0":
                one[i] = one[i-1] + 1 
            else: 
                one[i] += one[i-1]
       
        # Calculate the ways
        for i in range(len(s)):
            if s[i] == "0":
                ways += zero[i] * (zero[-1] - zero[i])
            else:
                ways += one[i] * (one[-1] - one[i])

        return ways