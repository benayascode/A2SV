# Problem: Unforgivable Curse (hard version) - https://codeforces.com/contest/1800/problem/E2

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
        self.parent = list(range(n))
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # Path compression
            x = self.parent[x]
        return x

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)



def solve():

    n, k = nsi()
    s = wi()
    t = wi()
    dsu = UF(n)

    for i in range(n):
        if i + k < n:
            dsu.union(i, i + k)
        if i + k + 1 < n:
            dsu.union(i, i + k + 1)
    # print(dsu.parent)
    

    grp = defaultdict(list)
    for i in range(n):
        grp[dsu.find(i)].append(i)
    # print(grp)
   
    for val in grp.values():
        ss = sorted(s[i] for i in val)
        tt = sorted(t[i] for i in val)
        if ss != tt:
            return print("NO")
    
    return print("YES")



ttt = ni()
for _ in range(test(ttt)):
    solve()

