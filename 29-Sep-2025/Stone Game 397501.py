# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def rec(i,j):
            if (i,j) in dp:
                return dp[(i,j)]

            if i > j:
                return 0
            
            turn = 0 if (j-i)%2 else 1

            if turn:
                dp[(i,j)] = max(rec(i+1,j) + piles[i], rec(i,j-1) + piles[j])

            else:
                dp[(i, j)] = max(rec(i + 1, j), rec(i, j - 1))
            return dp[(i, j)]
        
        a = rec(0,len(piles)-1)
        x = sum(piles) 

        return a > x-a

        
                