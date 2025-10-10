# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        check = sorted(heights)
        c = 0
        for i in range(len(heights)):
            if heights[i] != check[i]:
                c += 1
        return c
        