# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        mydict = {}
        for i in range(len(s)):
            mydict[indices[i]] = s[i]
        mydict = dict(sorted(mydict.items() , key = lambda x:x[0]))
        return "".join(list(mydict.values()))