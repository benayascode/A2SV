# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [0] * n
        mydict = {0:0}
        hp = [(0,0)]
        out = 0

        def manhat(a,b):
            return(abs(a[0]-b[0])+abs(a[1]-b[1]))

        while hp:
            w,u = heapq.heappop(hp)
            if visited[u] or mydict.get(u,float("inf")) < w:
                continue
            
            visited[u] = 1
            out += w

            for i in range(n):
                if not visited[i]:
                    mini = manhat(points[u],points[i])
                    if mini < mydict.get(i,float("inf")):
                        mydict[i] = mini
                        heapq.heappush(hp,(mini,i))
        
        return out


        