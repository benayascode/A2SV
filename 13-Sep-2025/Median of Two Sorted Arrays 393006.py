# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        add=len(nums1)+len(nums2)
        nums1.extend(nums2)
        nums1=sorted(nums1)
        if add%2==0:
            return (nums1[add//2-1]+nums1[add//2])/2
        else:
            return(nums1[add//2])/1
        