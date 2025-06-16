# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        out = 0
        
        for i in instructions:

            l = bisect_left(nums,i)
            r = bisect_right(nums,i)
            out += min(l , len(nums)-r)
            # print(l,r,out)
            bisect.insort(nums, i)
            
        return out % (10**9 + 7)