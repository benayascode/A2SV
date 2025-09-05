# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        f = 0
        def rec(i,j,k):
            nonlocal f
            if i == n:
                return j >= 2
                
            
            for num in range(i,n):
                t = int(s[i:num+1])
                if k == float("inf") or t + 1 == k:
                    if rec(num+1,j+1,t):
                        f = 1
                        return True
                # else:
                #     return rec(i+1,j,t) and  f

            return False
            
                   
        return(rec(0,0,float("inf")))
                


