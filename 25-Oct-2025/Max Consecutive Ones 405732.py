# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        cnt = 0
        for i in nums:
            if i:
                cnt += 1
            else:
                x = max(x,cnt)
                cnt = 0
        x = max(x,cnt)
        return x