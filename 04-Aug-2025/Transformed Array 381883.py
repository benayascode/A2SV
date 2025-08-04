# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                res[i] = nums[(nums[i] + i) % len(nums)]
            elif nums[i] == 0:
                res[i] = nums[i]
            else:
                res[i] = nums[(i - abs(nums[i]))% len(nums)]
        return res