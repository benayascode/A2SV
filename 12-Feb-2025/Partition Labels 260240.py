# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first ,  last = {} , {}
        for i,j in enumerate(s):
            if j not in first:
                first[j] = i
        for i,j in enumerate(s):
            last[j] = i
        overlap = []
        for i in first:
            overlap.append([first[i],last[i]])
        overlap.sort()
        out = []
        l , r = overlap[0]
        for start , end in overlap:
            if start <= r:
                r = max( r , end)
            else:
                out.append(r - l + 1)
                l , r = start , end
        out.append(r - l + 1)
        return out
