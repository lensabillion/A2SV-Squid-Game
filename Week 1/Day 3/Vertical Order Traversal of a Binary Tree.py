# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root,0,0)])
        hash_map = {}
        temp = []
        ans = []
        cols = set()
        while q:
            ins = []
            for i in range(len(q)):
                curr, row, col = q.popleft()

                if curr.left:
                    q.append((curr.left,row+1,col-1))
                if curr.right:
                    q.append((curr.right, row+1, col+1))
                ins.append((curr.val, col))
                if col not in hash_map:
                    hash_map[col] = []
               
                cols.add(col)
                
            temp.append(ins)

        for i in temp:            
            for j in sorted(i):
                hash_map[j[1]].append(j[0])
        cols = sorted(cols)
       
        for el in cols:          
            ans.append(hash_map[el])
        return ans