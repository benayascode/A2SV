# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mydict = {}
        c = 0 
        for i in answers:
            if i == 0:
                c += 1
            else:
                if i not in mydict or i == mydict[i]:
                    mydict[i] = 0
                    c += i + 1
                else:
                    mydict[i] += 1
        return c