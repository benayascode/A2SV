# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        out = k
        
        i = 0
        while i <= len(blocks) - k:
            c = 0
            for j in blocks[i:i+k]:
                if j == "W":
                    c += 1
            out = min(out , c)
            i += 1
        return out


        