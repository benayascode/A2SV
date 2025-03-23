# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxk: int) -> int:
        out = 0
        s,l,r = -1 ,-1,-1
        for i,j in enumerate(nums):
            if not mink <= j <= maxk:
                s = i
            else:
                if j == mink:
                    l = i
                if j == maxk:
                    r = i
            out += max(0,min(l,r)-s)
        return out
