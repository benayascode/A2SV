# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row , col = len(matrix) , len(matrix[0])
        out = []
        r , d , l , u = col-1 , row-1 , 0, 0

        while u <= d and l <= r:
            for j in range(l,r+1):
                out.append(matrix[u][j])
            u += 1
            
            for j in range(u,d+1):
                out.append(matrix[j][r])
            r -= 1

            if u <= d:
                for j in range(r,l-1,-1):
                    out.append(matrix[d][j])
                d -= 1

            if l <= r:
                for j in range(d,u-1,-1):
                    out.append(matrix[j][l])
                l += 1
        return out
        