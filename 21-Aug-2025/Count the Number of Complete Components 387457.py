# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        out = 0
        visited = set()


        def dfs(i,lst):
            if i in visited:
                return
            visited.add(i)
            lst.append(i)
            for j in adj[i]:
                dfs(j, lst)
            return lst

        
        for v in range(n):
            if v in visited:
                continue
            x = dfs(v, [])
            for i in x:
                if len(x) - 1 != len(adj[i]):
                    break
            else:out += 1
        return out