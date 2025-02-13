# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        out = 0
        l , r , c= 0 , 0 , 0
        while r < len(nums):
            if nums[r] == 0:
                c += 1
            if c > k:
                if nums[l] == 0:
                    c -= 1
                l += 1
            if c <= k:
                out = max(out , r - l + 1 )
            r += 1
        return out