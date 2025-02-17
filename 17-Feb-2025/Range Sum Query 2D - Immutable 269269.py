# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.premat = [] 
        for r in range(len(matrix)):
            x = []
            for c in range(len(matrix[0])):
                if r == 0 and c == 0:
                    x.append(matrix[r][c])
                elif r > 0  and c == 0:
                    x.append(matrix[r][c] + self.premat[r-1][c])
                elif c > 0 and r == 0:
                    x.append(x[-1] +matrix[r][c])
                elif r > 0 and c > 0:
                    x.append(matrix[r][c]+self.premat[r-1][c] + x[-1]-self.premat[r-1][c-1])
            self.premat.append(x)


        print(self.premat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1 == 0 and row1 == 0:
            return self.premat[row2][col2]
        if col1 == 0:
            return self.premat[row2][col2] - self.premat[row1-1][col2]
        if row1 == 0:
            return self.premat[row2][col2] - self.premat[row2][col1-1]
            
        return self.premat[row2][col2] - self.premat[row1-1][col2] - self.premat[row2][col1-1] + self.premat[row1-1][col1-1]
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)