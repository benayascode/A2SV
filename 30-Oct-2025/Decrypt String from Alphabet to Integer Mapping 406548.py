# Problem: Decrypt String from Alphabet to Integer Mapping - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        out = ""
        n = len(s)
        i = n-1
        while i >= 0:
            if s[i]== "#":
                x = int(s[i-2]+s[i-1])
                print(x)
                out += chr(96+x)
                i -= 3
            else:
                out += chr(96+int(s[i]))
                i -= 1
        return out[::-1]


            



        