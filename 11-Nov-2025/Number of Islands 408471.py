# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m= len(grid), len(grid[0])

        def dfs(x,y):
            if grid[x][y] == "-" or grid[x][y] == "0":
                return False
            
            grid[x][y] = "-"

            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    dfs(nx,ny)
            
            return True


        out = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    if dfs(i,j):
                        out += 1
            
        return out
