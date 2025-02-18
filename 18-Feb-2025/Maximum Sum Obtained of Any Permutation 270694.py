# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10**9 + 7
        maxi = max(i for j,i in  requests)
        pre = [0] * (maxi +2)

        for a,b in requests:
            pre[a] += 1
            pre[b+1] -= 1


        for i in range(1,len(pre)):
            pre[i] += pre[i-1]
        pre.sort()
        nums.sort()
        x = -1
        out = 0
        for i in range(len(pre)-1,0,-1):
            out += (nums[x] * pre[i])%mod
            out %= mod
            x -= 1
        return out%mod

