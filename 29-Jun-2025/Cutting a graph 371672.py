# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

import math, sys,heapq
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

'''



'''
class UF:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx,ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx

        elif self.rank[ry] > self.rank[rx]:
            self.parent[rx] = ry

        else:
            self.parent[rx] = ry
            self.rank[ry] += 1


def solve():
    n,m,k = nsi()
    graph = set()
    for _ in range(m):
        a,b = nsi()
        if a > b:
            a,b = b,a
        graph.add((a,b))
    
    opr = []
    out = set()

    for i in range(k):
        q,a,b = wsi()
        a, b = int(a), int(b)
        if a > b:
            a,b = b,a
        opr.append((q,a,b))
        if q == "cut":
            out.add((a,b))

    uf = UF(n)
    for a,b in graph:
        if (a,b) not in out:
            uf.union(a,b)
    # print(opr)
    res = []

    for i in range(k-1,-1,-1):
        q,a,b = opr[i]
        if q == "ask":
            res.append(yn(uf.find(a) == uf.find(b)))
        else:
            uf.union(a,b)
    res = reversed(res)
    print(*res,sep="\n")


    return

ttt = 1
for _ in range(test(ttt)):
    solve()