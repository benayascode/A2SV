# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        for i in range(1 , len(nums)):
            out[i] = nums[i-1] * out[i-1]
        r = 1
        for i in range(len(nums)-2,-1,-1):
            r *= nums[i+1]
            out[i] *=  r
        return out