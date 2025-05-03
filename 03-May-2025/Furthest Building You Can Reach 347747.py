# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        p = []
        i = 0
        for i in range(len(heights) - 1):
            x = heights[i + 1] - heights[i]
            
            if x <= 0:
                continue
            
            bricks -= x
            x = heapq.heappush(p, -x)
            print(x)
            if bricks < 0:
                bricks += -heapq.heappop(p)
                ladders -= 1
                
            if ladders < 0:
                return i
        return len(heights)-1