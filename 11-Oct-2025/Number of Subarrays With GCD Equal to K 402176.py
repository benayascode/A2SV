# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        c = 0
        n = len(nums)

        for i in range(n):
            curr = 0
            for j in range(i,n):
                curr = gcd(curr, nums[j])
                if curr == k:
                    c += 1
                
                if curr < k or curr % k != 0:
                    break
        return c