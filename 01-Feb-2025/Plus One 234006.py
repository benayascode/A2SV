# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        add=0
        out=[]
        for i in digits:
            add=add*10+i
        add=add+1
        while add>0:
            dig=add%10
            add=add//10
            out.insert(0,dig)
        return out