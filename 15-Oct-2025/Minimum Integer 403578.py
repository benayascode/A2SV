# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

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
    l,r,d = nsi()
    if d >= l:
        print((r//d + 1) * d)
    else:
        print(d)


    return

ttt = ni()
for _ in range(test(ttt)):
    solve()