# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

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
    f = 1
    for i in range(n):
        if i%2:
            if f:
                s = "."*(m-1)+"#"
                print(s)
                f = 0
            else:
                s = "#"+"."*(m-1)
                print(s)
                f = 1



        else:
            print(m*"#")


    return

ttt = 1
for _ in range(test(ttt)):
    solve()