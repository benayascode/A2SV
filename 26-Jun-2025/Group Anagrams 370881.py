# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)  
        for i in strs:
            key = tuple(sorted(i))  
            mydict[key].append(i)
        return list(mydict.values())
        