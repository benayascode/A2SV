# Problem: Restore the Array From Adjacent Pairs - https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        grf = defaultdict(list)
        for u,v in adjacentPairs:
            grf[v].append(u)
            grf[u].append(v)


        s = -1
        for k,v in grf.items():
            if len(v) == 1:
                s = k
                break
        
        out = []
        seen = set()

        def dfs(n):
            seen.add(n)
            for i in grf[n]:
                if i in seen:
                    continue
                dfs(i)
            out.append(n)
        dfs(s)
        return out