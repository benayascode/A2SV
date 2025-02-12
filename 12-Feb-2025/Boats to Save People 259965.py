# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l ,r = 0 , len(people)-1
        c = 0
        
        while l <= r:
            w = people[r] + people[l]
            if w <= limit:
                c += 1
                l += 1
                r -= 1
            else:
                r -= 1
                c += 1
        return c