# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        mydict = defaultdict(list)

        for j in range(n):
            for i in range(m):
                mydict[i + j].append(mat[i][j])
        
        out = []
        for i in range(m + n):
            if i % 2 == 0:
                out += mydict[i]
            else:
                out += mydict[i][::-1]
        return out
                    