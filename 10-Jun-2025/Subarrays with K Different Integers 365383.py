# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            out = 0                
            mydict = {}                  
            l = 0                    
            for r in range(len(nums)):
                mydict[nums[r]] = mydict.get(nums[r], 0) + 1
                while len(mydict) > k:
                    mydict[nums[l]] -= 1
                    if mydict[nums[l]] == 0:
                        del mydict[nums[l]]  
                    l += 1

                out += (r - l + 1)
            return out

        return helper(nums, k) - helper(nums, k - 1)