# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UF:
    def __init__(self, n):
        self.count = n              
        self.parent = list(range(n))
        self.rank = [1]*n           
        
    def find(self, p):
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q):
        x, y = self.find(p), self.find(q)
        if x == y: return False
        self.count -= 1 
        if self.rank[x] > self.rank[y]: x, y = y, x
        self.parent[x] = y
        self.rank[y] += self.rank[x] 
        return True
    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UF(n) 
        bob = UF(n) 
        
        out = 0
        edges.sort(reverse=True) 
        for t, u, v in edges: 
            u, v = u-1, v-1
            if t == 3:
                out += not (alice.union(u, v) and bob.union(u, v)) 
            elif t == 2:
                out += not bob.union(u, v)                     
            else:
                out += not alice.union(u, v)                            
        return out if alice.count == 1 and bob.count == 1 else -1