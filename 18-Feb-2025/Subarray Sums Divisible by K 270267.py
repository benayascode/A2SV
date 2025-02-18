# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mydict = Counter([0])
        cur_sum = 0
        out = 0

        for i in nums:
            cur_sum += i
            out += mydict[(cur_sum % k)]
            mydict[cur_sum%k] += 1
        return out
            
        