# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scr = sorted(score)
        scr.reverse()
        mydict = {}
        for i,j in enumerate(scr):
            mydict[j] = (i+1)
        # print(mydict)
        out = [""] * len(score)
        for i in range(len(score)):
            if mydict[score[i]] == 1:
                out[i] = "Gold Medal"
            elif mydict[score[i]] == 2:
                out[i] = "Silver Medal"
            elif mydict[score[i]] == 3:
                out[i] = "Bronze Medal"
            else:
                out[i] = str(mydict[score[i]])
        return out
