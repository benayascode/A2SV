# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(ind, curr):
            if ind == len(nums):
                return 1 if curr == target else 0
            
            if (ind, curr) in memo:
                return memo[(ind, curr)]
            
            ad = dp(ind+1, curr + nums[ind])
            sub = dp(ind+1, curr - nums[ind])

            memo[(ind, curr)] = ad +sub

            return ad + sub
        
        return dp(0, 0)