# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = [0] * len(nums1)
        for i in range(len(nums1)):
            nums[i] = nums1[i]-nums2[i]
        self.c = 0
        def merge(left_arr, right_arr):
            i, j = 0, 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j] + diff:
                    print(left_arr[i], right_arr[j])
                    self.c += len(right_arr) - j
                    i += 1
                else:
                    j += 1

            l, r = 0, 0
            merged_arr = []
            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l] < right_arr[r]:
                    merged_arr.append(left_arr[l])
                    l += 1
                else:
                    merged_arr.append(right_arr[r])
                    r += 1
            return merged_arr + left_arr[l:] + right_arr[r:]
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            m = len(arr)//2
            left_arr = merge_sort(arr[:m])
            right_arr = merge_sort(arr[m:])
            return merge(left_arr, right_arr)
        
        merge_sort(nums)
        return self.c