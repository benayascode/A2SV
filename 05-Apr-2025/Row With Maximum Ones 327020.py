# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxi = 0
        out = [0,0]
        for i,j in enumerate(mat):
            c = sum(j)
            if maxi < c : 
                out = [i,c ] 
                maxi = c 
        return out