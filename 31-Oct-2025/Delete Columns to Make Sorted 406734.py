# Problem: Delete Columns to Make Sorted - https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        out=[]
        for i in range(len(strs[0])):
            for j in strs:
                out.append(j[i])
            x=out
            if out != sorted(x):
                count+=1
            out=[]
        return count
            
        