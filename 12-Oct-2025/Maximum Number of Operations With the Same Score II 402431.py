# Problem: Maximum Number of Operations With the Same Score II - https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        x,y,z = nums[0] + nums[1], nums[-1] + nums[-2], nums[0]+nums[-1]
        memo = {}

        def dp(l,r,x):
            if (l, r, x) in memo:
                return memo[(l,r,x)]

            a,b,c = 0,0,0

            if l >= n or r < 0:
                return -1
            if r-l+1 <  2:
                return 0
            
            if nums[l] + nums[l+1] == x:
                a = 1 + dp(l+2,r, x)
            if nums[r] + nums[r-1] == x:
                b = 1 + dp(l,r-2, x)
            if nums[l] + nums[r] == x:
                c = 1 + dp(l+1, r-1, x)

            memo[(l,r,x)] = max(a,b,c)
            return memo[(l, r, x)]
        return max(dp(0,n-1, x), dp(0,n-1, y), dp(0,n-1, z))



            

            
        
            