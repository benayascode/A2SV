# Problem: Merge Sort - https://codeforces.com/problemset/problem/873/D

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
    n, k = nsi()
    
    if k % 2 == 0 or k > 2 * n - 1:
        return print(-1)
        
    out = list(range(1, n + 1))
    c = 1
    def helper(l, r):
        nonlocal c
        if k == c:
            return
        if l + 1 >= r:
            return
        mid = (l + r) // 2
        out[mid - 1], out[mid] = out[mid], out[mid - 1]
        c += 2
        helper(l, mid)
        helper(mid, r)
    
    helper(0, n)

    print(*out)

    return

ttt = 1
for _ in range(test(ttt)):
    solve()