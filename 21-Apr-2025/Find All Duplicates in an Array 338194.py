# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        ans = []
        while i<n:
            correct = nums[i]-1
            if nums[i]!=nums[correct]:
                nums[i],nums[correct] = nums[correct],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!= i+1:
                ans.append(nums[i])
        return ans