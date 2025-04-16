# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        arr = defaultdict(int)

        for i in employees:
            graph[i.id].extend(i.subordinates)
            arr[i.id] = i.importance

        def dfs(node):
            out = 0
            for nei in graph[node]:
                out += arr[nei] + dfs(nei)
            return out

        return arr[id] + dfs(id)