# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        chars = "abcdefghijklmnopqrstuvwxyz"

        pre = [0] * len(s)
        for a,b,c in shifts:
            if c == 0:
                pre[a] -= 1
                if b < len(s)-1:
                    pre[b+1] += 1
            else:
                pre[a] += 1
                if b < len(s)-1:
                    pre[b+1] -= 1
        print(pre)
        
        for i in range(1,len(s)):
            pre[i] = pre[i] + pre[i-1]

        s = list(s)
        
        for i in range(len(s)):
            ind = chars.index(s[i])
            s[i] = chars[(ind+pre[i])%26]

        return "".join(s)
        




