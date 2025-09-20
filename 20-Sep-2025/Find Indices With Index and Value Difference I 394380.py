# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n=len(nums)
        l,r=0,0

        while r<n:
            if abs(l-r)>=indexDifference and abs(nums[l]-nums[r])>=valueDifference:
                return [l,r]
            
            r+=1
            if r==n and l<n-1:
                l+=1
                r=l       
        return [-1,-1]