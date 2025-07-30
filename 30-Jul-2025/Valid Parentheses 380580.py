# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i == ")":
                if stack and stack.pop()=="(":
                    continue
                else:
                    return False
            elif i=="]":
                if stack and stack.pop()=="[":
                    continue
                else:
                    return False
            else:
                if stack and stack.pop()=="{":
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        return False

            
        