class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # Intitalize answer matrix 
        ans = [[0 for _ in range(len(mat[0])) ] for _ in range(len(mat))]
        
        # Prefix sum of the given matrix
        for i in range(1, len(mat[0])):
            mat[0][i] += mat[0][i-1]        
        for i in range(1, len(mat)):
            mat[i][0] += mat[i-1][0]
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                mat[i][j] += (mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1])
        # Populate the answer matrix from the prefix sum  

        for row in range(len(mat)):
            sr = max(0, row - k)
            er = min(len(mat) - 1, row + k)
            for col in range(len(mat[0])):
                sc =max(0, col - k)
                ec = min(len(mat[0]) - 1, col + k)
              
                if sc - 1 >= 0 and sr - 1 >= 0:
                    ans[row][col] = (mat[er][ec] - (mat[sr-1][ec] + mat[er][sc - 1])) + mat[sr-1][sc-1]
                elif sc - 1 >= 0:
                    ans[row][col] = mat[er][ec] - mat[er][sc - 1]
                elif sr - 1 >= 0:
                    ans[row][col] = mat[er][ec] - mat[sr-1][ec]
                else:
                     ans[row][col] = mat[er][ec]
        return ans
                