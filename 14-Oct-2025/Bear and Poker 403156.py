# Problem: Bear and Poker - https://codeforces.com/problemset/problem/574/C

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
    def helper(x):
        while not x % 2:
            x //= 2
        while not x % 3:
            x //= 3
        return x
    y = helper(a[0])
    for i in range(1,n):
        x = helper(a[i])
        if y != x:
            return print("No")
    print("Yes")



    return

ttt = 1
for _ in range(test(ttt)):
    solve()