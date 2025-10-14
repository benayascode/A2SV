# Problem: Little Girl and Maximum Sum - https://codeforces.com/problemset/problem/276/C

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
    n,q = nsi()
    a = nsi()
    arr = [0] * (n+1)
    for i in range(q):
        l,r = nsi()
        arr[l-1] += 1
        arr[r] -= 1
    # print(arr)
    for i in range(1,n+1):
        arr[i] += arr[i-1]
    arr.sort()
    a.sort()
    # print(arr,a)
    c = 0
    for i in range(n-1,-1,-1):
        if arr[i+1] == 0:
            return print(c)
        c += (arr[i+1]*a[i])
        # print(a[i])
    print(c)



    return

ttt = 1
for _ in range(test(ttt)):
    solve()