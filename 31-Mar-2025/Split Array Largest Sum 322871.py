# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(m):
            c = 1
            curr = 0
            for i in nums:
                curr += i
                if curr > m:
                    c += 1
                    curr = i
                    if c > k:
                        return False
            return True

        l , r = max(nums) , sum(nums)
        while l <= r:
            m = (l+r)//2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l