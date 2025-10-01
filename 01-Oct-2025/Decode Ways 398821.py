# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        if s[0] == "0":
            return 0
        
        dp[0] += 1
        dp[1] += 1
        
        for i in range(2,n+1):
            if 9 < int(s[i-2:i]) < 27:
                dp[i] += dp[i-2]
            if int(s[i-1]):
                dp[i] += dp[i-1]

        # print(dp)
        
        return dp[n]
            
