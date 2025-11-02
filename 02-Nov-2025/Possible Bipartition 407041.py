# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        mydict = defaultdict(set)
        for i,j in dislikes :
            mydict[i].add(j)
            mydict[j].add(i)
        
        visited = dict()

        for node in range(1,n+1):
            if node not in visited:
                q = deque([(node,True)])
                while q:
                    i, col = q.popleft()
                    visited[i] = col
                    for j in mydict[i]:
                        if j in visited:
                            if visited[j] == col :
                                return False
                        else:
                            visited[j] = not col
                            q.append((j, not col))
        
        return True
        

        