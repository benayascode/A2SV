# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        dr = [(0,1), (1,0), (-1,0), (0,-1)]
        arr = [[0]*col for _ in range(row)]

        q = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    arr[i][j] = -1  

        while q:
            r, c = q.popleft()
            for x, y in dr:
                nr, nc = r + x, c + y
                if 0 <= nr < row and 0 <= nc < col and arr[nr][nc] == -1:
                    arr[nr][nc] = arr[r][c] + 1
                    q.append((nr, nc))
        return arr
