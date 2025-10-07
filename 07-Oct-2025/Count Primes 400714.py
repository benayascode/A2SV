# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        arr = [1]*(n)
        i = 2
        while (i*i) < n:
            if arr[i]:
                for j in range(i*i,n,i):
                    arr[j] = 0
            i += 1
        return arr.count(1) - 2