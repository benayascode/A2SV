# Problem: Count ways to group overlapping ranges - https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        out = [ranges[0]]
        
        for s1, e1 in ranges[1 : ]:
            s2, e2 = out[-1]
            
            if max(s1, s2) <= min(e1, e2):
                out[-1] = [min(s1, s2), max(e1, e2)]
            else:
                out.append([s1, e1])
        
        return pow(2, len(out), pow(10, 9) + 7)