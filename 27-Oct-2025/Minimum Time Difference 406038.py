# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        hours = []
        for i in timePoints:
            hours.append(int(i[0:2])*60 + int(i[3:5]))
        hours.sort()
        mini = float('inf')
        for i in range(len(hours)-1):
            x =hours[i+1] - hours[i]
            mini = min(mini , x)
        x = ((24*60)-hours[-1]) +  hours[0]
        mini = min(mini , x)

        return mini