# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

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
    a = nsi()
    b = nsi()


    b.sort()
    if a[0] > b[0]-a[0]:a[0] = b[0] - a[0]

    # print(a)
    for i in range(1,n):
        x = a[i]+a[i-1]
        l = bisect_left(b,x)
        # print(l)
        if l < m and (b[l]-a[i]<a[i]or a[i]<a[i-1]):
            a[i] = b[l] - a[i]
        if a[i] < a[i-1]:
            return print("NO")
    print("YES")


    



    return

ttt = ni()
for _ in range(test(ttt)):
    solve()