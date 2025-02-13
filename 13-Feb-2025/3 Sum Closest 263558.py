# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        x = float('inf')
        for i in range(len(nums)-1):
            l = i+1
            r = len(nums)-1
            while(l<r):
                total = nums[i] + nums[l] +nums[r]
                if total == target:
                    return target
                elif abs(target - total) < x : 
                    x = abs(target-total)
                    ans = total
                if total > target:
                    r -= 1
                else:
                    l += 1
        return ans