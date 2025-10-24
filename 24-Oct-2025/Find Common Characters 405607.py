# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        out=list(words[0])
        j=0
        while j < len(words):
            i=0
            while i<len(out):
                if out[i] not in words[j]:
                    out.pop(i)
                else:
                    words[j]=words[j].replace(out[i],"",1)
                    i+=1
                    
            j+=1
        return out
        