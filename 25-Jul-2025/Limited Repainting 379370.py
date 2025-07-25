# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

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
    n,k = nsi()
    s = wi()
    a = nsi()
    out = 0

    def helper(m):
        x = "R"
        c = 0
        for i in range(n):
            if a[i] > m:
                if s[i] == "B" and x == "R":
                    c += 1
                x = s[i]
        return c <= k


    low,high = 0, max(a)
    while high >= low:
        mid = (high+low)//2

        if helper(mid) :
            out = mid
            high = mid-1
            
        else:
            low = mid+1
            
    print(out)
            


    return

ttt = ni()
for _ in range(test(ttt)):
    solve()