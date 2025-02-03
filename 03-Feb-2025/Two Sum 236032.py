# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, nums in enumerate(nums):
            if target - nums not in mydict:
                mydict[nums] = i
            else:
                return [mydict[target-nums] , i]
        return []
