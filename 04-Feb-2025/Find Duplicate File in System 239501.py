# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)

        for pa in paths:
            p = pa.split()
            folder = p[0]
            for j in p[1:]:
                val , key = j.split(".txt")
                mydict[key].append((folder,val))
        print(mydict)
        out = []
        for k , v in mydict.items():
            temp = []
            if len(v) > 1:
                for f,n in v:
                    s = f+"/"+n+".txt" 
                    temp.append(s)
                out.append(temp)
        return out        