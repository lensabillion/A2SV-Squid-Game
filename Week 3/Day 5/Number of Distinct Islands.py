#User function Template for python3
from collections import deque
import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        
        shapes = set()
        queue = []
        
        n = len(grid)
        m = len(grid[0])
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    shape = []
                    
                    while queue:
                        row, col = queue.pop(0)
                        for nr, nc in (row + 1, col), (row - 1, col), (row, col +  1), (row, col - 1):
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                                queue.append((nr, nc))
                                shape.append((nr - r, nc - c))
                                grid[nr][nc] = 0

                    shapes.add(tuple(shape))
                    
        return len(shapes)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends