# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):return []
        pdict = Counter(p)
        k = len(p)
        count = []
        sdict = {}

        for j in range(0,k):
            if s[j] not in sdict:
                sdict[s[j]] = 0
            sdict[s[j]] += 1
        if sdict == pdict:
            count.append(0)


        for l in range(1,len(s)-k+1):
            if sdict[s[l-1]] == 1:
                del sdict[s[l-1]]
            else:
                sdict[s[l-1]] -= 1

            if s[l+k-1] not in sdict:
                sdict[s[l+k-1]] = 0
            sdict[s[l+k-1]] += 1

            if pdict == sdict:
                count.append(l)
            
        return count


            
