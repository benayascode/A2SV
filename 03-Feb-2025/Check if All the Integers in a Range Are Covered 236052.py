# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for i , j in ranges:
            if j < left:
                continue
            if i > left:
                return False
            if j >= right:
                return True
            left = max(left ,j+1)
        return False