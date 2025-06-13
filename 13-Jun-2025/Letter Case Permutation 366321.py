# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
       
        n = len(s)
        set_ = set() 
        out = []


        for i in range(2 ** n):
            x = ""
            for j in range(n):
                if (i >> j) & 1:
                    x += s[j].upper()
                else:
                    x += s[j].lower()

            if x not in set_:  
                out.append(x)
                set_.add(x)
                
        return out