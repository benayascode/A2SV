# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l ,r , i = 0 , len(nums)-1 , 0
        while i <= r:
            if nums[i] == 0:
                temp = nums[l]
                nums[l] = 0
                nums[i] = temp
                l += 1
                i += 1
            elif nums[i] == 2:
                temp = nums[r]
                nums[r] = 2
                nums[i] = temp
                r -= 1
            else:
                i += 1
        