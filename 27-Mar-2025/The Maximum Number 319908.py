# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        if len(nums)<=2:
            return max(nums)
        if len(nums)<3:
            return min(nums)
        nums=sorted(nums)
        return nums[len(nums)-3]