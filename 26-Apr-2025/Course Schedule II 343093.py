# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = [0] * numCourses
        queue = deque()
        out,c = [0]*numCourses,0

        for a,b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)

        while queue:
            q = queue.popleft()
            out[c] = q
            c += 1

            for i in graph[q]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    queue.append(i)

        if c == numCourses:
            return out
        return []
            