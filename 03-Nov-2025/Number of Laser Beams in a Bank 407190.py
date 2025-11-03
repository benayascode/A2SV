# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        out = 0
        x = 0
        for i in bank:
            c = i.count('1')
            if c:
                out += x*c
                x = c
        return out

        