# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

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
    n, m = nsi()
    if n < m:
        return print(-1)
    mini = math.ceil(n / 2) 

    for i in range(mini, n + 1):
        if i % m == 0:
            return print(i)

    print(-1)

    return

ttt = 1
for _ in range(test(ttt)):
    solve()