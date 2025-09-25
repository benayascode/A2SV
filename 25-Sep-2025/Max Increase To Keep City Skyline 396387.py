# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row = [max(i) for i in grid]
        col = [max(i) for i in zip(*grid)] 

        out = 0
        for r in range(n):
            for c in range(n):
                out += min(row[r], col[c]) - grid[r][c]

        return out