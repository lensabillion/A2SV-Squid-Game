import heapq
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        h = []
        ans = [0] * (2050 + 1)

        for alive in logs:
            b = alive[0]
            d = alive[1]

            ans[b] += 1
            ans[d] -= 1
        for i in range(1950, len(ans)):
            ans[i] += ans[i-1]
        for i in range(1950, len(ans)):
            heapq.heappush(h, (-ans[i], i))
        return heapq.heappop(h)[1]
    