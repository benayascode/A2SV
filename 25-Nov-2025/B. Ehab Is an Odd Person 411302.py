# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

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
    n = ni()
    a = nsi()
    e,o = 0,0
    for i in a:
        if i % 2:
            o += 1
        else:
            e += 1
        if o and e:
            return print(*sorted(a))
    print(*a)


    return

ttt = 1
for _ in range(test(ttt)):
    solve()