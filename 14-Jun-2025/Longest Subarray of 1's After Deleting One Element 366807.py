# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        c = 0 
        l = 0
        lis = []
        for i in nums:
            if i == 1:
                c += 1
            else:
                lis.append(c)
                c = 0
        if c:lis.append(c)

        if len(lis) == 1:
            return len(nums)-1
        maxi = 0
        for i in range(len(lis)-1):
            maxi = max(maxi,lis[i]+lis[i+1])
        return maxi