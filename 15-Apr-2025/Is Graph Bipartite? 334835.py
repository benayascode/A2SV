# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool: 
        col = [-1] * len(graph) 
        flag = True  

        def dfs(i, c):
            nonlocal flag
            if not flag:
                return
            
            col[i] = c
            # print(col,i)
            for nbr in graph[i]: 
                if col[nbr] == -1: 
                    if c == 0 :
                        cc = 1
                    else:
                        cc = 0
                    dfs(nbr, cc) 
                elif col[nbr] == col[i]:  
                    flag = False 

        
        for i in range(len(graph)):
            if not flag:
                return False
            if col[i] == -1: 
                dfs(i, 0)

        return True  