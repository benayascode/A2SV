# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        for i in range(len(questions)-1, -1, -1):
            ind = i + questions[i][1] + 1
            if ind < len(questions):
                dp[i] = dp[ind] + questions[i][0]
            else:
                dp[i] = questions[i][0]
            if i < len(questions) - 1:
                dp[i] = max(dp[i+1],dp[i])
        return dp[0]