# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        x = self.getRow(rowIndex-1)
        c = [1]+ [x[i] + x[i-1] for i in range(1,len(x))]+[1]
        return c
            