# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        out = []
        for l, r in intervals:
            out.append((l, 1))   
            out.append((r + 1, -1))  
        
        out.sort()
        grp = 0
        curr = 0
        for a, b in out:
            curr += b
            grp = max(grp, curr)
        
        return grp
        