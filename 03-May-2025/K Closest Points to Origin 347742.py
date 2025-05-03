# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        out = []
        for i in range(len(points)):
            a,b = points[i]
            points[i] = [a**2+b**2 , a,b]
        heapq.heapify(points)
        while k:
            r,a,b = heapq.heappop(points)
            out.append([a,b])
            k -= 1
        return out

        