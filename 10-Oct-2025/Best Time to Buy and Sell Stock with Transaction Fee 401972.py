# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        c, out = -1 *  (5 * 10**4), 0 
        for i in prices:
            c = max(c, out-i)
            out = max(out, c + i - fee)
        return out