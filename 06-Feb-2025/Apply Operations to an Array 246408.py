# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
                i+=2
            else:
                i+=1
        x=nums.count(0)
        nums=[i for i in nums if i != 0]
        nums = nums + [0] * x
        return nums
        