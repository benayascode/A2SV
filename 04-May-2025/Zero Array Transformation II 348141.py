# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)
        def valid(m):
            pre = [0] * (n+1)
            for a,b,c in queries[:m]:
                pre[a] += c
                pre[b+1] -= c

            for i in range(n):
                pre[i+1] += pre[i]
                if pre[i] < nums[i]:
                    return False
            return True

        l , r = 0,q
        while l <= r:
            m = (l+r) // 2
            if valid(m):
                r = m - 1
            else:
                l = m+1
        if l > q:
            return -1
        return l