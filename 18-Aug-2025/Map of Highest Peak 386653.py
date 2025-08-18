# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        out = [[-1] * n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i, j, 0))
                    out[i][j] = 0

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c, h = q.popleft()
            for x, y in dirs:
                nr, nc = r + x, c + y
                if 0 <= nr < m and 0 <= nc < n and out[nr][nc] == -1:
                    out[nr][nc] = h + 1
                    q.append((nr, nc, h + 1))

        return out


