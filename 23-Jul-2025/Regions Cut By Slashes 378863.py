# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        row,col = len(grid), len(grid[0])
        row2, col2 = 3*row, 3*col
        mat = [[0]*col2 for _ in range(row2)]

        for i in range(row):
            for j in range(col):
                r, c = i*3, j*3
                if grid[i][j] == "/":
                    mat[r][c+2] = 1
                    mat[r+1][c+1] = 1
                    mat[r+2][c] = 1
                elif grid[i][j] == "\\":
                    mat[r][c] = 1
                    mat[r+1][c+1] = 1
                    mat[r+2][c+2] = 1

        def dfs(r,c,visited):
            if r<0 or c<0 or r == row2 or c == col2 or (r,c) in visited or mat[r][c] != 0:
                return
            
            visited.add((r,c))
            dr = [(0,1),(1,0),(-1,0),(0,-1)]
            for x,y in dr:
                dfs(r+x,c+y,visited)

        out = 0
        visited = set()
        for r in range(row2):
            for c in range(col2):
                if mat[r][c] == 0 and ((r,c) not in visited):
                    dfs(r,c,visited)
                    out += 1
        return out



