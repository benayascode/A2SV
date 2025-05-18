# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        
        x = 1 << len(nums)

        for i in range(x):
            temp = []
            for j in range(len(nums)):
                if i & (1 << j):
                    temp.append(nums[j])
            out.append(temp)
        return out