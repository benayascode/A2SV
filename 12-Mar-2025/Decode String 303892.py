# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = 0
        t=""
        for i in s:
            if i.isdigit():
                n = n * 10 + int(i)
            elif i=='[':
                stack.append((n,t))
                n = 0
                t = ""
            elif i==']':
                n,x = stack.pop()
                t = x +n*t
                n=0
            else:
                t += i
            # print(t)
            # print(stack)
        return t    