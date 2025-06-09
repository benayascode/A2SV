# Problem: Count Complete Subarrays in an Array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l = len(set(nums))
        n = len(nums)
        c = 0
        for i in range(n):
            check = set()
            for j in range(i,n):
                check.add(nums[j])
                if len(check) == l:
                    c += (n-j)
                    break
        return c