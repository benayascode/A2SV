# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

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
def solve():
    n,m = nsi()
    a =nsi()
    b = nsi()
    out = [0]*m
    

    x = 0
    for i in a:
        x = math.gcd(i-a[0],x)
    
    for j in range(m):
        out[j] = math.gcd(a[0]+b[j],x)
    print(*out)


    return

ttt = 1
for _ in range(test(ttt)):
    solve()