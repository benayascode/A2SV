# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        out = 0

        for i in range(0,len(nums)):
            node = heapq.heappop(nums)
            if node < k:
                out += 1
                x = heapq.heappop(nums)
                heapq.heappush(nums,node*2+x)
            else:
                break
        return out