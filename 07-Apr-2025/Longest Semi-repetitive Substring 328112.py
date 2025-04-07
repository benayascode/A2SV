# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        res = 0
        out = [1]
        for i in range(1,len(s)):
            if ( s[i]==s[i-1]):
                out.append(1)
            else:
                out[-1]=out[-1]+1
        for j in range(1,len(out)):
            res = max(res,out[j]+out[j-1])
        
        return max(res,out[0])