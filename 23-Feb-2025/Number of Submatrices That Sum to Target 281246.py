# Problem: Number of Submatrices That Sum to Target - https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]

        count = 0

        for i in range(n):
            for j in range(i, n):
                mydict = {0: 1}
                sum_val = 0

                for row in range(m):
                    sum_val += matrix[row][j] - (matrix[row][i - 1] if i > 0 else 0)
                    count += mydict.get(sum_val - target, 0)
                    mydict[sum_val] = mydict.get(sum_val, 0) + 1

        return count