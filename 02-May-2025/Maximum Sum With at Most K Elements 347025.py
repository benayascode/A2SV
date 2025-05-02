# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        hp = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                heapq.heappush(hp,(-grid[r][c],r))
        out = 0

        while k and hp:
            val,r = heapq.heappop(hp)
            if limits[r] == 0:
                continue
            limits[r] -= 1

            out += -val
            k -= 1
        return out