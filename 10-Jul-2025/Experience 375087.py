# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

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

'''




'''

class UF:
    def __init__(self, n):
        self.p = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.add = [0] * (n + 1)
        self.dif = [0] * (n + 1)

    def find(self, x):
        if self.p[x] != x:
            rt = self.find(self.p[x])

            self.dif[x] += self.dif[self.p[x]]
            self.p[x] = rt
        return self.p[x]

    def join(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.size[xr] < self.size[yr]:
            xr, yr = yr, xr

        self.p[yr] = xr
        self.size[xr] += self.size[yr]

        self.dif[yr] = self.add[xr] - self.add[yr]
        self.add[yr] = 0



def solve():
    n, m = nsi()

    uf = UF(n)

    for _ in range(m):
        q = wsi()
        if q[0] == "get":
            x = int(q[1])
            uf.find(x)
            print(uf.add[uf.p[x]] - uf.dif[x])

            # print(uf.p)
            # print(uf.add)
            # print(uf.dif)
            

        elif q[0] == "join":
            x, y = int(q[1]), int(q[2])
            uf.join(x, y)

        else:
            x, val = int(q[1]), int(q[2])
            rt = uf.find(x)
            uf.add[rt] += val
        # print(uf.dif)
        # print(uf.add)
            

    return

ttt = 1
for _ in range(test(ttt)):
    solve()

