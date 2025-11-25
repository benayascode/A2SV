# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = []
        mini,maxi = intervals[0][0], intervals[0][1]

        for i in range(1,len(intervals)):
            x,y = intervals[i]
            if x <= maxi:
                maxi = max(maxi,y)
            else:
                out.append([mini,maxi])
                mini,maxi = x,y
        out.append([mini,maxi])
        return out