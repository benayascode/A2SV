# Problem: Freedom Trail - https://leetcode.com/problems/freedom-trail/

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def dfs(i, p):
            if i == len(key):
                return 0
            res = float('inf')
            for j in pos[key[i]]:
                x = abs(p - j)
                step = min(x, n - x) + 1
                res = min(res, step + dfs(i + 1, j))
            return res
    
        n = len(ring)
        pos = defaultdict(list)
        for i, j in enumerate(ring):
            pos[j].append(i)

        return dfs(0, 0)