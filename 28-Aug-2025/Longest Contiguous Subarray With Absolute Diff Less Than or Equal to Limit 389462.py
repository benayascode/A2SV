# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        out,l = 0 , 0
        queue_min , queue_max = deque() , deque()

        for r,i in enumerate(nums):
            while queue_max and queue_max[-1] < i:
                queue_max.pop()
            queue_max.append(i)

            while queue_min and queue_min[-1] > i:
                queue_min.pop()
            queue_min.append(i)

            while queue_max[0] - queue_min[0] > limit:
                if queue_max[0] == nums[l]:
                    queue_max.popleft()
                if queue_min[0] == nums[l]:
                    queue_min.popleft()

                l += 1
            out = max(out,r-l+1)

        return out            
