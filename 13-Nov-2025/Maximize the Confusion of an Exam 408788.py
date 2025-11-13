# Problem: Maximize the Confusion of an Exam - https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxi = 0
        l,r = 0, 1
        mydict = {'T':0, 'F':0}
        n = len(answerKey)
        if n == 1: return 1
        mydict[answerKey[0]] += 1

        while r < n:
            mydict[answerKey[r]] += 1
            if (r - l + 1) - max(mydict['T'], mydict['F']) > k:
                

                mydict[answerKey[l]] -= 1
                l += 1
            maxi = max(maxi, r-l+1)
            r += 1
        return maxi
