# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        out=[]
        for i in operations:
            if i =="C":
                out.pop()
            elif i == "D":
                out.append(int(out[len(out)-1]*2))
            elif i=="+":
                out.append(int(out[len(out)-1]+out[len(out)-2]))
            else:
                out.append(int(i))
        return sum(out)
        