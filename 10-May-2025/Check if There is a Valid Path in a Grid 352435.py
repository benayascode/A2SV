# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        r,c = len(grid),len(grid[0])
        drs = {1:[(0,-1),(0,1)],2:[(1,0),(-1,0)],3:[(0,-1),(1,0)],
                    4:[(0,1),(1,0)],5:[(0,-1),(-1,0)],6:[(0,1),(-1,0)]}
        q = deque()
        visited = set()
        q.append((0,0))
        visited.add((0,0))
        while q:
            x,y=q.popleft()
            if x == r-1 and y == c-1:
                return True
            for dx,dy in drs[grid[x][y]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < r and 0 <= ny < c and (nx,ny) not in visited:
                    if (-dx,-dy) in drs[grid[nx][ny]]:
                        q.append((nx,ny))
                        visited.add((nx,ny))
        return False