# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        out = 0
        for i, j in enumerate(manager):
            graph[j].append(i)

        def dfs(i,x):
            nonlocal out
            x += informTime[i]
            if x > out:
                out = x
            for j in graph[i]:
                dfs(j,x)
        
        dfs(headID,0)
        return out
