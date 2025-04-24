# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = {}
        out = []

        def dfs(i):
            if i in visited:
                return visited[i]
            visited[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            
            visited[i] = True
            return True


        for i in range(n):
            if dfs(i):
                out.append(i)
        
        return out
