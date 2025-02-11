# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        mydict = {}
        s_nums = sorted(nums)
        for i in range(len(nums)):
            if s_nums[i] not in mydict:
                mydict[s_nums[i]] = i
            
        for i,j in enumerate(nums):
            out[i] = (mydict[j])

        return out


        