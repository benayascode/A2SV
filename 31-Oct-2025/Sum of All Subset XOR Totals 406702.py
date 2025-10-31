# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        out = 0
        n = len(nums)
        for i in nums:
            out |= i
            print(out)
        return out * (2**(n-1))