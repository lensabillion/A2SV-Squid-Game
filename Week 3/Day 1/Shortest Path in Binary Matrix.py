import heapq
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        h = []
        dir = [(0,1), (1,0), (1, -1), (-1, 1),(-1,0),(0,-1), (1,1), (-1,-1)]
        visited = set()
        if grid[0][0] == 0:
            heapq.heappush(h,(1, 0, 0))
            visited.add((0,0))
        
        def isValid(i, j):
            if 0 <= i < len(grid) and 0<= j < len(grid[0]) and (i, j) not in visited and grid[i][j] == 0:
                return True
            return False
        while h:
            cd, cr, cc = heapq.heappop(h)
            
            if cr == len(grid)-1 and cc == len(grid[0])-1:
                return cd
            for d in dir:
                nr = cr + d[0]
                nc = cc + d[1]
                nd = cd + 1
                if isValid(nr, nc):
                    visited.add((nr, nc))
                    heapq.heappush(h,(nd, nr, nc))
        return -1