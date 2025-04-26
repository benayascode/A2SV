# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = [0] * numCourses
        queue = deque()
        out = 0

        for a,b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)

        while queue:
            q = queue.popleft()
            out += 1

            for i in graph[q]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    queue.append(i)
        
        return out == numCourses



