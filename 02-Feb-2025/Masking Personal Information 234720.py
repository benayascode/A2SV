# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            n , d = s.split("@")
            n = n.lower()
            d = d.lower()
            return n[0]+"*****"+n[-1]+"@"+d
        else:
            out = ""
            for i in s:
                if i.isdigit():
                    out += i
            if len(out) > 10:
                return "+"+"*"*(len(out)-10)+"-***-***-"+out[-4:]
            return "***-***-"+out[-4:]