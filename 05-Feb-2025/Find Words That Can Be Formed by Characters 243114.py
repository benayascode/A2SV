# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        out = 0
        f = 1
        for i in words:
            c = Counter(chars)
            f = 1
            for j in i:
                if j not in c:
                    f = 0
                    break
                if c[j] == 1:
                    del c[j]
                else:
                    c[j] -= 1
            if f:
                out += len(i)
        return out
                
        