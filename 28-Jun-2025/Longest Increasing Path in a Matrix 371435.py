# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix), len(matrix[0])
        arr = [[0]*m for i in range(n)]
        dir = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(i,j):
            if arr[i][j]:
                return arr[i][j]
            
            maxi = 1
            for x,y in dir:
                xx,yy = i+x , j+y
                if (0<=xx and xx<n) and (0<=yy and yy<m) and matrix[xx][yy] > matrix[i][j]:
                    maxi = max(maxi,1 + dfs(xx,yy))
            arr[i][j] = maxi
            return maxi
        out = 0
        for i in range(n):
            for j in range(m):
                out = max(out,dfs(i,j))
        return out