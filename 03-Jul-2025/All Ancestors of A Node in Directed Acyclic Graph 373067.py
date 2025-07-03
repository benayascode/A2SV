# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        out = [set() for _ in range(n)]
        indeg = [0] * n
        graph = defaultdict(list)


        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1

        q = deque()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for nei in graph[node]:
                out[nei] = out[nei].union(out[node], {node})
                indeg[nei] -= 1
                if not indeg[nei]:
                    q.append(nei)
                    
            out[node] = sorted(out[node])
        return out

