# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        mydict = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
        
        def find(x):
            if x != mydict[x]:
                mydict[x] = find(mydict[x])
            return mydict[x]
        
        def union(x, y):
            if x != mydict[x]:
                union(mydict[x], y)
            mydict[x] = y
            
        for a,b in zip(s1, s2):
            aa,bb = find(a), find(b)
            
            if aa > bb:
                union(aa, bb)
            else:
                union(bb, aa)

        return "".join([find(mydict[i]) for i in baseStr])