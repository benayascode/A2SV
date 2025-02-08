# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        out=[[0] * (n-2) for k in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                put=[grid[i][j],grid[i][j+1],grid[i][j+2],
                grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],
                grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]]
                out[i][j]=max(put)
        return out