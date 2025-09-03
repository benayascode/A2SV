# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:        
        left, right = 0, int(c**0.5)         
        while left <= right:
            out = left**2 + right**2
            if out == c:
                return True
            elif out < c:
                left += 1
            else:
                right -= 1       
        return False        