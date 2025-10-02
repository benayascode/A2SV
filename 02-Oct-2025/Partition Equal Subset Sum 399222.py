# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2: return False

        tot //= 2
        dp = [0] * (tot+1)
        dp[0] = 1

        for i in nums:
            for j in range(tot,i-1,-1):
                if dp[j]:
                    continue
                if dp[j-i]:
                    dp[j] = True
        if dp[-1]:
            return True
        return False
