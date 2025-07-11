# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1

        visited = set()
        for i,j in trust:
            visited.add(i)

        res = defaultdict(int)
        for i , j in trust:
            if j not in visited:
                out = j
                res[j]+=1

        if len(res) != 1:
            return -1
        if res[out] == n -1:
            return out
        return -1
