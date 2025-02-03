# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mydict = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        out = ""
        while columnNumber:
            columnNumber=columnNumber-1
            out=mydict[columnNumber%26]+out
            columnNumber=columnNumber//26
        return out