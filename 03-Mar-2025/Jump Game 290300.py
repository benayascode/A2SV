# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        l = n-1

        for i in range(n-1,-1,-1):
            k = nums[i]
            if i + k >= l:
                l = i
        return l == 0