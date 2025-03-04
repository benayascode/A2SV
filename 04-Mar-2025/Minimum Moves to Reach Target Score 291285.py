# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        out = 0
        while maxDoubles and target:
            if target % 2 != 0:
                out += 1
                target -= 1
            target //= 2
            if target >=1:
                out += 1
            
                
            maxDoubles -= 1
        out += (target-1)
        return out
