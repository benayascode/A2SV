# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt = 0
        mvs = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                cnt += 1
            else:
                mvs += cnt
        return mvs