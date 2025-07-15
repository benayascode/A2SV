# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

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
sys.setrecursionlimit(1 << 25)

'''



'''
def solve():
    n,m = nsi()
    par = list(range(n+2))
    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]
    # print(par)
    for _ in range(m):
        a,b = wsi()
        b = int(b)
        if a == "-":
            par[b] = find(b+1)
        else:
            if b > n:
                print(-1)
            else:
                out = find(b)
                if out > n:
                    print(-1)
                else:
                    print(out)




    return

ttt = 1
for _ in range(test(ttt)):
    solve()