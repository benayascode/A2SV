# Problem: E - Cycle in Graph - https://codeforces.com/gym/602812/problem/E

# Betel
import math, sys
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
from random import randint

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'
test = lambda inp=0: number() if not inp else inp
jasjdfh = randint(0, 100000)
xor = lambda x: x ^ jasjdfh
sys.setrecursionlimit(10**6)

 
 
def solve():
    n, m, k = numbers()
    graph = [[] for _ in range(n + 1)]
    # print(graph)
    for _ in range(m):
        u, v = numbers()
        graph[u].append(v)
        graph[v].append(u)
    # print(graph)

    visited = [0] * (n + 1)
    adj = [-1] * (n + 1)
    a = [0] * (n + 1)
    out = []

    def dfs(u, p):
        nonlocal out
        visited[u] = 1
        for v in graph[u]:
            if v == p:
                continue
            if visited[v]:
                if a[u] - a[v] + 1 >= k + 1 and not out:
                    x = []
                    cur = u
                    while cur != v:
                        x.append(cur)
                        cur = adj[cur]
                    x.append(v)
                    out = x
                    return
            else:
                adj[v] = u
                a[v] = a[u] + 1
                dfs(v, u)
                if out:
                    return

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1)
            if out:
                break

    print(len(out))
    print(' '.join(map(str, out)))
    
    return
 
for _ in range(test(1)):
    solve()