# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        out = 0
        def check(m):
            c = 0
            for i in candies:
                if i >= m:
                    c += (i // m)
            return c >= k

        l , r = 1 , max(candies)
        while l <= r:
            m = (l+r) // 2
            if check(m):
                l = m+1
            else:
                r = m - 1
        return l-1
