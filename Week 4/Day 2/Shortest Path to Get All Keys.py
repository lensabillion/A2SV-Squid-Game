from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        k = 0
        small = "abcdef"
        q = deque([])
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in small:
                    k += 1
                if grid[i][j] == "@":
                    q.append((0,i, j,""))
                    # seen.add((i, j))
        
        def isValid(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != "#":
                return True
            return False
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        # keys = []
        while q:
            # print(keys, steps)
            
            step, row, col, keys= q.popleft()
            # print(keys, row, col, step)
            if (row, col, keys) in seen:
                continue
            if len(keys) == k:
                return step
            seen.add((row, col, keys))
            for dr in dir:
                nr = row + dr[0]
                nc = col + dr[1]
                if isValid(nr, nc):
                    curr = grid[nr][nc]
                    # print(curr,  curr.lower() in keys )
                    if grid[nr][nc] in ".@":
                        q.append((step + 1, nr, nc, keys))
                    elif grid[nr][nc].lower() in keys:
                        q.append((step + 1, nr, nc, keys))
                        # seen.add((nr, nc))
                    elif grid[nr][nc] in small:
                        # keys.append()
                        if grid[nr][nc] not in keys:
                            q.append((step + 1, nr, nc, keys + grid[nr][nc]))
                        else:
                            q.append((step + 1, nr, nc, keys))
            
                    # print( q)
            # seen.add((row, col))
        return -1


        