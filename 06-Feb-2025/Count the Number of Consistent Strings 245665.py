# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        alw = set(allowed) 
        count = 0
        
        for w in words:
            if set(w).issubset(alw):
                count += 1
        
        return count