# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:
        def gettowork(m):
            cur , c = 0 , 0
            for i in w:
                cur += i
                if cur > m:
                    c += 1
                    cur = i
            return c



        l,r = max(w) , sum(w)
        while l <= r:
            m = (l+r) // 2
            if gettowork(m) < days:
                r = m-1
            else:
                l = m+1
        return l
