# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        out = 0
        mydict, csum = Counter([0]), 0
        for i in nums:
            csum += i
            out += mydict[csum-k]
            mydict[csum] += 1     
        return out   
        