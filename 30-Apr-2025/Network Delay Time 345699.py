# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        m = n
        visited = set()
        for u,v,t in times:
            graph[u].append((v,t))
        hp = [(0,k)]
        out = 0

        while hp:
            w,n = heapq.heappop(hp)
            if n in visited:
                continue
            out = max(out,w)
            visited.add(n)

            for nn,ww in graph[n]:
                if nn not in visited:
                    heapq.heappush(hp,(ww+w,nn))

        print(len(visited),out)

        return out if len(visited) == m else -1
        