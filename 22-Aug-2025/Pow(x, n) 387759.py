# Problem: Pow(x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = 0
        if n < 0:
            neg = 1
            n *= -1

        def pow(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n%2 == 0:
                x *= x
                return pow(x,n/2)
            return x * pow(x,n-1)
        if neg:
            return 1/pow(x,n)
        return pow(x,n)