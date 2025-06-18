# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UF:
    def __init__(self, s):
        self.s = s
        self.p = list(range(s))
        self.l = [-1] * (s)
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        small, big = (rx, ry) if self.l[rx] < self.l[ry] else (ry, rx)
        self.p[small] = big
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UF(n)
        
        edgeList.sort(key=lambda x: x[2])
        out = [None] * len(queries)
        queries = [(l, s, d, i) for i, (s, d, l) in enumerate(queries)]
        queries.sort(key=lambda x:x[0])
        
        ind = 0
        for l, i, j, idx in queries:
            while ind < len(edgeList) and edgeList[ind][2] < l:
                uf.union(edgeList[ind][0], edgeList[ind][1])
                ind += 1
            
            out[idx] = uf.find(i) == uf.find(j)
        
        return out