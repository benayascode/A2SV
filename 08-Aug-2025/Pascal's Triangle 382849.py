# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:return []
        out = [[1]]
        for i in range(1,numRows):
            prv = out[-1]
            temp = [1]

            for j in range(1, len(prv)):
                temp.append(prv[j-1]+prv[j])
            temp.append(1)
            out.append(temp)
        return out