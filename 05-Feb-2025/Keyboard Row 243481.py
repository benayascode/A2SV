# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        add = 1
        out = []

        for w in words:
            wor = w.lower()
            c = Counter(wor)
            if wor[0] in first:
                f = first
            elif wor[0] in second:
                f = second
            else:
                f = third
            for i in c:
                if i not in f:
                    break
            else:
                out.append(w)
        return out
            
                


        