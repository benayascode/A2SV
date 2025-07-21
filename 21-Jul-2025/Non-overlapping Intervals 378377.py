# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        s = 0
        c = 1
        for i in range(1, n):
            if intervals[i][0] >= intervals[s][1]:
                s = i
                c += 1

        return n - c