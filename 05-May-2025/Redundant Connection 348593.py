# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] > rank[ry]:
                parent[ry] = rx
                rank[rx] += rank[ry]
            else:
                parent[rx] = ry
                rank[ry] += rank[rx]
            return True
        
        for x, y, in edges:
            if not union(x, y):
                return [x, y]
