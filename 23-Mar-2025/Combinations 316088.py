# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        def rec(num , path):
            # print(path)
            if len(path) == k:
                out.append(path[:])
                return
            
            for i in range(num,n+1):
                path.append(i)
                rec(i+1,path)
                path.pop()
        rec(1,[])
        return out

        