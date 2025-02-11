# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left=nums[:mid]
            right=nums[mid:]
            sortleft=mergesort(left)
            sortright=mergesort(right)
            return merge(sortleft,sortright)
        def merge(left,right):
            result = []
            i = j = 0
            while len(left) > i and len(right) > j:
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        return mergesort(nums)