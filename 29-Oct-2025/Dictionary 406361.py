# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

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
    a,b = list(wi())

    x = ord(a) - 96
    y = ord(b) - 96
    z = 1 if x < y else 0
    print((x-1)*25 + y - z)

    return

ttt = ni()
for _ in range(test(ttt)):
    solve()