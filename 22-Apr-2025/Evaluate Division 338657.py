# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        for (a,b),v in zip(equations,values):
            graph[a].append((b,v))
            graph[b].append((a,1/v))

        def dfs(curr, target, total, visited):
            if curr == target:
                return total

            visited.add(curr)

            for nei,w in graph[curr]:
                if nei not in visited:
                    res = dfs(nei,target,total*w,visited)
                    if res != -1:
                        return res
            
            return -1

        out = []
        for x,y in queries:
            if x not in graph or y not in graph:
                out.append(-1.000)
                continue
            out.append(dfs(x,y,1,set()))
        return out