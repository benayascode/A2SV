# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/description/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        out=[]
        if len(nums)<2:
            return 0
        else:
            nums.sort()
            for i in range(1,len(nums)):
                out.append(nums[i]-nums[i-1])
        return max(out)
        