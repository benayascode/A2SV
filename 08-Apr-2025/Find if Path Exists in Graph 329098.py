# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        check = set()
        adj = [[]for i in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            if node == destination:
                return True

            check.add(node)
            for i in adj[node]:
                if i not in check:
                    x = dfs(i)

                    if x:
                        return True
            return False
        return dfs(source)
            