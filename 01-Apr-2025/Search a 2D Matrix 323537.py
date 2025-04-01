# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r , c = len(matrix) , len(matrix[0])
        l ,r = 0 , r * c - 1
        while l <= r:
            m = (l+r) // 2
            x = matrix[m//c][m%c]

            if x == target:
                return True
            elif x > target:
                r = m - 1
            else:
                l = m + 1
        return False
                    

        