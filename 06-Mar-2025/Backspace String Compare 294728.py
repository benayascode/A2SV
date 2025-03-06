# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s , stack_t = [] , []
        for i in s:
            if stack_s and i =="#":
                stack_s.pop()
            elif i != "#":
                stack_s.append(i)
        
        for i in t:
            if stack_t and i =="#":
                stack_t.pop()
            elif i != "#":
                stack_t.append(i)
        return stack_s == stack_t