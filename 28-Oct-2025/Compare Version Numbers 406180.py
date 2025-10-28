# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        n1, n2 = len(v1), len(v2)

        for i,j in zip(v1,v2):
            if int(i) < int(j):
                return -1
            if int(i) > int(j):
                return 1

        x = min(n1, n2)        
        if n1 < n2:
            return -1 if any(int(v2[i])>0 for i in range(x, n2)) else 0
        if n2 < n1:
            return 1 if any(int(v1[i])>0 for i in range(x, n1)) else 0
        return 0