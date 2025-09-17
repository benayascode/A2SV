# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        cnt = 0

        for i in range(0,len(nums)):
            l = nums[i]
            for j in range(i, len(nums)):
                l = lcm(l, nums[j])
                if l == k:
                    cnt += 1
                if l > k:
                    break
        return cnt