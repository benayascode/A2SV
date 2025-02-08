# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(row,len(matrix)):
                temp=matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        for row in matrix:
            row.reverse()