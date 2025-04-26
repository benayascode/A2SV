# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queue = deque()
        out = [False] * len(queries)
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[a].append(b)

        def helper(a, b, visited):
            if a == b:
                return True
            if a in visited:
                return False
            
            visited.add(a)
            for nei in graph[a]:
                if nei == b or helper(nei, b, visited):
                    return True
            return False

        ind = 0
        for a,b in queries:
            out[ind] = helper(a,b,set())
            ind += 1
        return (out)




