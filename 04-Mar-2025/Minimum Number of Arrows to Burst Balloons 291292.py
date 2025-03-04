# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        c = len(points)
        cur = points[0][1]

        for i in range(1,len(points)):
            if points[i][0] <= cur:
                cur = min(cur,points[i][1])
                c-=1
            else:
                cur = points[i][1]
        return c