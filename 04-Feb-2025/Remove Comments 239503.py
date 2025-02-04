# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        out, block = [], False
        s = ""
        for c in source:
            if not block: s = ""
            i, n = 0, len(c)
            while i < n:
                if block:
                    if c[i:i + 2] == '*/' and i + 1 < n:
                        i += 2
                        block = False
                        continue
                    i += 1
                else:
                    if c[i:i + 2] == '/*' and i + 1 < n:
                        i += 2
                        block = True
                        continue
                    if c[i:i + 2] == '//' and i + 1 < n:
                        break
                    s += c[i]
                    i += 1
            if s and not block:
                out.append(s)
                    
        return out
        