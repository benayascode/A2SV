# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mini = min(costs)
        maxi = max(costs)
        if mini > coins:
            return 0
        if mini == coins:
            return mini
        
        out = [0] *(maxi - mini+1)
        for i in costs:
            out[i-mini] += 1

        s_costs = []
        for i in range(len(out)):
            s = [i + mini] * out[i]
            s_costs.extend(s)
        
        cnt = 0
        out = 0
        for i in s_costs:
            if coins < cnt+i:
                return out
            cnt += i
            out += 1
        return out
       
