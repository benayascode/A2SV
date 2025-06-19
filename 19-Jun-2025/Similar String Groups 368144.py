# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        p = list(range(len(strs)))
        rank = [0] * len(strs)

        def find(x):
            if p[x] == x:
                return x
            p[x] = find(p[x])
            return p[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:

                if rank[rx] > rank[ry]:
                    p[ry] = rx
                elif rank[ry] > rank[rx]:
                    p[rx] = ry
                else:
                    p[ry] = rx
                    rank[rx] += 1

        def helper(x: str, y: str):
            cnt = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    cnt = cnt + 1
                    if cnt > 2:
                        return 0
            return 1

        out = len(strs)
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if find(i) != find(j) and helper(strs[i], strs[j]):
                    out -= 1
                    union(i, j)
        return out