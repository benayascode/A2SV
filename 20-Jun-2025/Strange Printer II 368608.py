# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        bounds = {}  



        for i in range(m):
            for j in range(n):
                col = targetGrid[i][j]
                if col not in bounds:
                    bounds[col] = [i, i, j, j]
                else:
                    bounds[col][0] = min(bounds[col][0], i)
                    bounds[col][1] = max(bounds[col][1], i)
                    bounds[col][2] = min(bounds[col][2], j)
                    bounds[col][3] = max(bounds[col][3], j)

        graph = defaultdict(set)
        indeg = defaultdict(int)

        for col, (r1, r2, c1, c2) in bounds.items():
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    x = targetGrid[i][j]
                    if x != col:
                        if x not in graph[col]:
                            graph[col].add(x)
                            indeg[x] += 1

        clr = set(bounds.keys())
        q = deque([i for i in clr if indeg[i] == 0])
        out = set()

        while q:
            c = q.popleft()
            out.add(c)
            for nei in graph[c]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        return len(out) == len(clr)
