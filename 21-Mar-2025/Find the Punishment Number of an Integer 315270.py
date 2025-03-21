# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:

        def helper(i):
            j = str(i * i)
            l = len(j)

            def rec(start, x):
                if start == l:
                    return x == i  
                
                for ind in range(start, l):
                    t = int(j[start:ind + 1])
                    if x + t > i:
                        return False 
                    if rec(ind + 1, x + t):
                        return True
                
                return False

            return rec(0, 0)

        out = 0  
        for i in range(1, n + 1):
            if helper(i):
                out += i * i
        return out

                
                    


