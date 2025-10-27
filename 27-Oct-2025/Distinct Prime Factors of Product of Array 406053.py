# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        set_ = set()
        def prime(n):
            while n % 2 == 0:
                set_.add(2)
                n //= 2
            
            i = 3
            limit = math.sqrt(n)

            while i <= limit:
                while n % i == 0:
                    set_.add(i)
                    n //= i
                i += 2
            if n > 1:
                set_.add(n)
        
        for i in nums:
            prime(i)
        return len(set_)