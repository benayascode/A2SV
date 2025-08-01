# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        nxt = 1
        for i in coins:
            if nxt - i < 0:
                break
            nxt += i
        return nxt