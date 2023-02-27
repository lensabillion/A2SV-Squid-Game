import heapq
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        h = []
        ans = 0
        energy = 0
        for task in tasks:
            heapq.heappush(h, (-1 * (task[1]-task[0]),task))
        # print(h)
        while h:
            gap, task = heapq.heappop(h)

            if energy < task[1]:
                ans += task[1] - energy
                energy = -1 * gap
            else:
                energy -= task[0]
        return ans