# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in redEdges:
            graph[a].append((b,"red"))
        for a,b in blueEdges:
            graph[a].append((b,"blue"))

        out = [-1]*n
        visited = set()
        q = deque([(0,0,None)])

        while q:
            node,d,e = q.popleft()
            visited.add((node,e))
            if out[node] == -1:
                out[node] = d
            for nei,i in graph[node]:
                if (nei,i) not in visited and e != i:
                    q.append((nei,d+1,i))

        return out