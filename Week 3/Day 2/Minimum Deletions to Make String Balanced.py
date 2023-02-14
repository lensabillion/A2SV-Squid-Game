class Solution:
    def minimumDeletions(self, s: str) -> int:
        a, b = 0, 0 
        for i in s:
            if i == "a":
                b += 1
        ans = b

        for i in range(1, len(s) + 1):
            if s[i - 1] == "b":
                a += 1
            else:
                b -= 1
            ans = min(ans, a + b)

        return ans
        