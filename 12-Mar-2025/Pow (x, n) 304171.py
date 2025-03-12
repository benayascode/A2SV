# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        f = 0
        if n < 0:
            f = 1
            n = -1 * n
        self.x = x
        
        def pow(x,n):
            if n == 0 :
                return 1
            if n == 1:
                return x
            if n % 2 == 0: 
                x = x*x
                return  (pow(x,n/2)) 
            else:
                return x * (pow(x,n-1))
        if f:
            return 1/pow(x,n)
        return pow(x,n)
        