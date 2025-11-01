# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        out = 0
        for i in range(min(n,limit)+1):
            s = max(0,n-i-limit)
            e = min(n-i, limit)
            out += max(0,e - s + 1)
        return out