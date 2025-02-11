# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lcnt = 0
        x = nums.count(target)

        for i in nums:
            if i < target:
                lcnt += 1
        return list(range(lcnt,lcnt+x))