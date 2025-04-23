# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time,fresh = 0,0
        n,m = len(grid),len(grid[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))

        while q and fresh: 

            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in direction:
                    nr,nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))
            time += 1
        return -1 if fresh else time

