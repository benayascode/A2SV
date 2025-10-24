# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        out=""
        for i in range(len(s)-1,-1,-1):
            out=out+s[i]+" "
        return out[:-1]

        