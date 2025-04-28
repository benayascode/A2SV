# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

import math, sys
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
from random import randint

ni = lambda: int(sys.stdin.readline().strip())
nsi = lambda: list(map(int, sys.stdin.readline().strip().split()))
wsi = lambda: sys.stdin.readline().strip().split()
wi = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'
test = lambda inp=0: ni() if not inp else inp
randkey = randint(0, 100000)
xor = lambda x: x ^ randkey
sys.setrecursionlimit(10**6)  

'''



'''
def solve():
    n, m = nsi()
    g = [[] for _ in range(n)]
    deg = [0] * n
    visited = [0] * n

    for _ in range(m):
        x, y = nsi()
        x -= 1
        y -= 1
        g[x].append(y)
        g[y].append(x)
        deg[x] += 1
        deg[y] += 1

    def dfs(i, nei):
        visited[i] = 1
        nei.append(i)
        for j in g[i]:
            if not visited[j]:
                dfs(j, nei)

    ans = 0
    for i in range(n):
        if not visited[i]:
            nei = []
            dfs(i, nei)
            if all(deg[v] == 2 for v in nei):
                ans += 1

    print(ans)


    return

ttt = 1
for _ in range(test(ttt)):
    solve()