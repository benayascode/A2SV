# Problem: Count Subarrays Where Max Element Appears at Least K Times - https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        c = 0
        l = 0
        out = max(nums)
        
        for i in nums:
            if i == out:
                k -= 1
            while k ==0:
                if nums[l] == out:
                    k += 1
                l += 1
                
            c += l
            
        return c    