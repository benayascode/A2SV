# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        r = 0  
        c = 0 
        players.sort()
        trainers.sort()
        
        for i in players:
            while r < len(trainers) and trainers[r] < i:
                r += 1 
            
            if r < len(trainers):
                c += 1  
                r += 1  
        
        return c
