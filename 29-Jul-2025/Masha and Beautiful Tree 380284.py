# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

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
    c = 0 


    def rec(arr,l,r):
        if r-l == 1:
            return 0
        
        m = (l+r)//2
       
        left = rec(arr,l,m)
        right =rec(arr,m,r)
        c = 0
        x = arr[l:m]
        y = arr[m:r]

        if x[0] > y[0]:
            for i in range(m - l):
                arr[l + i], arr[m + i] = arr[m + i], arr[l + i]
            c = 1
           
        return left+right+c
        
    x = rec(a,0,n)
    # print(a,x)
    if a == sorted(a):
        print(x)
    else:
        print(-1)
        




    return

ttt = ni()
for _ in range(test(ttt)):
    solve()