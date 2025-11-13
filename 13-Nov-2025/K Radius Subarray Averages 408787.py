# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # return [-1]
        n =  len(nums)
        out = [-1] * n
        x = 2*k+1
        if x > n:
            return out

        tot = 0
        for i in range(2*k+1):
            tot += nums[i]
        out[k] = tot//x
        # print(tot)
        j = 0

        for i in range(k+1 ,n-k):
            tot -= nums[j]
            # print(tot)
            tot += nums[i+k]
            # print(tot)
            out[i] = tot//x
            j += 1
            

        return out
