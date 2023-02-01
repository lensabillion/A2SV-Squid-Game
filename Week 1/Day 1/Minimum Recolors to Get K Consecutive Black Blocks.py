class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = 0
        for i in range(k):
            if blocks[i] == "W":
                ans += 1
        local = ans
        for i in range(k, len(blocks)):
            if  blocks[i-k] == "W":
                local -= 1
            if blocks[i] == "W":
                local += 1
            ans = min(ans, local)
        return ans