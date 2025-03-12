# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def bt(l,r):
            if l > r:
                return 0
            
            left = nums[l] + min(bt(l+1,r-1), bt(l+2, r))
            right = nums[r] + min(bt(l,r-2), bt(l+1, r-1))
            return max(left,right)

        return bt(0, len(nums) - 1) >= sum(nums)/2
