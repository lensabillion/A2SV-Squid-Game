import heapq
class Solution:
    def racecar(self, target: int) -> int:
        h = [(0, 0, 1)]
        visited = set()
        visited.add((0, 1))

        while h:
            cnt, p, s = heapq.heappop(h)
            if p == target:
                return cnt
            #A
            if (p+s, s*2) not in visited and p + s >= 0:
                heapq.heappush(h, (cnt + 1, p + s, s * 2 ))
                visited.add((p + s, s * 2 ))
            #R
            if s > 0:
                if (p, -1) not in visited and p < 2 * target:
                    heapq.heappush(h, (cnt + 1, p , -1 ))
                    visited.add((p , -1))
               
            else:
                if (p, 1) not in visited and p < 2 * target:
                    heapq.heappush(h, (cnt + 1, p, 1 ))
                    visited.add((p , 1))
               