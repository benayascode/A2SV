# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        maxi = 0


        def dfs(i,j):
            if i < 0 or i >= n or j < 0 or j >= m or (i, j) in visited or grid[i][j] == 0:
                return 0
            visited.add((i,j))
            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxi = max(maxi,dfs(r,c))
        
        return maxi
