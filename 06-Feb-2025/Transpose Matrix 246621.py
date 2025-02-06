# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        out=[]
        put=[]
        for i in range(len(matrix[0])):
            for j in matrix:
                out.append(j[i])
            put.append(out)
            out=[]
        return put
            
        