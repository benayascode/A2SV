# Problem: Make Sum Divisible by P - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        mydict = {0:-1}
        x = total % p
        if not x:
            return 0
        c = float('inf')
        pre = 0


        for i in range(len(nums)):
            pre = (pre + nums[i]) % p
            k = (pre - x + p) % p
            if  k in mydict:
                c = min(c,i - mydict[k])
            mydict[pre] = i
        return c if c < len(nums) else -1
