# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mydict = Counter([0])
        cur_sum = 0
        out = 0

        for i in nums:
            cur_sum += i
            out += mydict[(cur_sum-goal)]
            mydict[cur_sum] += 1
        return out
        