# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        add=0
        check=0
        for i in range(len(nums)+1):
            add+=i
        for i in range(len(nums)):
            check+=nums[i]
        return (add-check)
        