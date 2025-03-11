# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            if n == 0:
                return 1
            out = n * fact(n-1)
            return out

        num = fact(n)
        c = 0
        while num > 0:
            if num%10:
                break
            c += 1
            num //=10
        return c


        