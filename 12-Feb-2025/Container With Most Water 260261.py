# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1 
        res=0 
        while l<r:
            res=max(res,(r-l)*min(height[l],height[r])) 
            if height[l]<height[r]: 
                l+=1
            else:
                r-=1
        return res        