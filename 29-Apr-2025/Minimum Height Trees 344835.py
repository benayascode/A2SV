# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        out = []
        mydict = {}
        queue = deque()
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        # print(graph)
        for i,nei in  graph.items():
            if len(nei) == 1:
                queue.append(i)
            mydict[i] = len(nei)

        while queue:
            if n <= 2:
                return list(queue)
            for _ in range(len(queue)):
                q = queue.popleft()
                n -= 1
                for i in graph[q]:
                    mydict[i] -= 1
                    if mydict[i] == 1:
                        queue.append(i)

        
