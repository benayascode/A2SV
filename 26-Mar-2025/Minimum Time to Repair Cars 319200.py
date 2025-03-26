# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def valid(m):
            total=0
            for i in ranks:
                x = int(sqrt(m/i))
                total += x
            return total >= cars
                
        l = min(ranks)
        r = max(ranks)*cars*cars
        while l <= r:
            m =(l+r)//2
            if valid(m):
                r = m - 1
            else:
                l = m + 1
        return l