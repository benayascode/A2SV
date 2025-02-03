# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        out = []
        s = s.split()
        w = ""
        i = 0
        j = 0
        maxi = max([len(m) for m in s])

        while i < maxi:
            w = ""
            j = 0
            while j < len(s):
                
                if len(s[j]) > i:
                    w += s[j][i]
                else:
                    w += " "
                j += 1
            i += 1
            for l in range(len(w)-1,-1,-1):
                if w[l] != " ":
                    break
            out.append(w[:l+1])
        return out
                    