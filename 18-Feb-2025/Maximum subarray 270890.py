# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        out = float('-inf')
        l = 0
        print(nums)

        for i in range(len(nums)):
            
            out = max(out,nums[i])

            if i > 0 and nums[i-1] < nums[l] and (out - nums[i-1]) >= 0:
                l = i-1
            x = nums[i]-nums[l] if i != l else out
            out = max(out,x)
        return out