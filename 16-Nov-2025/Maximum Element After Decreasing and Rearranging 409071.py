# Problem: Maximum Element After Decreasing and Rearranging - https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        maxi = 1
        for i in range(1,len(arr)):
            if arr[i] > maxi:
                maxi += 1

        return maxi