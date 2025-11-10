# Problem: Ugly Number - https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:return True
        if n < 1:return False
        fact = set()
        while n % 2 == 0:
            fact.add(2)
            n //= 2
        limit = int(math.sqrt(n)) + 1
        for i in range(3,limit):
            while n % i == 0:
                fact.add(i)
                n //= i
        if n:
            fact.add(n)
        
        seen = {2,3,5,1}
        for i in fact:
            if i not in seen:
                return False
        return True
        