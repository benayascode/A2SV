# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mydict = Counter(nums)
        return [i for i in nums if mydict[i]==1]
        