# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        s = list(s)
        mydict = Counter(s)
        mydict = dict(sorted(mydict.items(), key = lambda x:x[-1] , reverse = True))
        s = [i * val for i,val in mydict.items()]
        return "".join(s)