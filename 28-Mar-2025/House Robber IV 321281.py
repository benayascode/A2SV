# Problem: House Robber IV - https://leetcode.com/problems/house-robber-iv/

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def check(m):
            _k = k
            i = 0
            while i < len(nums):
                if nums[i] <= m:
                    i+=2
                    _k -= 1
                    if _k == 0:
                        return True
                else:
                    i+=1
            return False

        l = min(nums)
        r = max(nums)

        
        while l <= r:
                m = (l+r)//2
                if check(m):
                    r = m-1
                else:
                    l = m+1
        return l
        
        