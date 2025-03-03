# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        r , l = 0 ,0 
        for i in s:
            if i == "L":
                l += 1
            else:

                r += 1
            if r == l:
                cnt += 1
                l = 0
                r = 0
        return cnt
        