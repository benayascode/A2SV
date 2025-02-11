# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        out = 0
        l , r = 0 , len(piles)-1
        while l < r:
            out += piles[r-1]
            r -= 2
            l += 1
        return out

        
