# Problem: Team Composition: Programmers and Mathematicians - https://codeforces.com/problemset/problem/1611/B

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
    a, b = nsi()
    print(min(a, b, (a + b) // 4))

    return

ttt = ni()
for _ in range(test(ttt)):
    solve()