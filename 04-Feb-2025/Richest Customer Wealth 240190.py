# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result=0
        out=[]
        for i in accounts:
            for j in i:
                result+=j
            out.append(result)
            result=0
        return max(out)
        