# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def helper(n):
            if n == 0:
                return 1
            if n == -1:
                return 0
            step1 = helper(n-1)
            step2 = helper(n-2)
            # print(step1,step2)
            return (step1+step2)
        return helper(n)
        
        