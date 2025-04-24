# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n = len(quiet)
        out = [-1] * n

        for a,b in richer:
            graph[b].append(a)

        def dfs(i):
            if out[i] != -1:
                return out[i]


            out[i] = i
            for nei in graph[i]:
                mini = dfs(nei)
                if quiet[mini] < quiet[out[i]]:
                    out[i] = mini
            return out[i]

        for i in range(n):
            dfs(i)
        return out
       


        
