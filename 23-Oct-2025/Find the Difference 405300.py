# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mydict = {}
        for i in s:
            if i not in mydict or mydict[i] == 0:
                mydict[i] = 1
            else:
                mydict[i] = 0
        for i in t:
            if i not in mydict or mydict[i] == 0:
                mydict[i] = 1
            else:
                mydict[i] = 0
        for k , v in mydict.items():
            if v == 1:
                return k
        return ""
