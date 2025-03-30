# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()

        def check(m):
            i , j = 0, 0
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <= m:
                    i += 1
                else:
                    j += 1
            return i == len(houses)
                    
                
        l , r = 0 , max(houses[-1],heaters[-1])
        while l <= r:
            m = (l+r) // 2
            if check(m):
                r = m - 1
            else:
                l = m + 1


        return l