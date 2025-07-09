# Problem: Hongcow Builds A Nation - https://codeforces.com/contest/744/problem/A

import math, sys, heapq
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



"""



"""

def solve():
    n, m, k = nsi()
    gvrn = nsi() 

    par = list(range(n + 1))

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]


    for _ in range(m):
        u, v = nsi()
        ru, rv = find(u), find(v)
        if ru != rv:
            par[rv] = ru

    size = [0] * (n + 1)
    for i in range(1, n + 1):
        size[find(i)] += 1

    tot = n
    out = 0
    c = 0

    visited = set()
    # print(size)

    for x in gvrn:
        d = find(x)
        if d in visited:
            continue

        visited.add(d)

        c = max(c, size[d])
        
        num = size[d]
        out += num * (num - 1) // 2
        tot -= size[d]

    out -= c * (c - 1) // 2
    num = c + tot
    out += num * (num - 1) // 2
    out -= m

    print(out)

ttt = 1
for _ in range(test(ttt)):
    solve()
