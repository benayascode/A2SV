# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        hp = []
        out , x = [], 0
        for i,(j,k) in enumerate(tasks):
            heapq.heappush(hp,(j,k,i))

        hp2 = []
        while hp  or hp2:
            while hp and hp[0][0] <= x:
                a,b,i = heapq.heappop(hp)
                heapq.heappush(hp2,(b,i))
            if hp2:
                a,b = heapq.heappop(hp2)
                out.append(b)
                x += a
            elif hp:
                x = hp[0][0]
        return out