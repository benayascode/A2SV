# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

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

    def pf(n):
        fct = {}
        while not n%2:
            fct[2] = fct.get(2,0) + 1
            n //= 2
        i , limit = 3, math.sqrt(n)
        while i <= limit:
            while n % i == 0:
                fct[i] = fct.get(i,0) + 1
                n //= i
                limit = math.sqrt(n)
            i += 2

        if n > 1:
            fct[n] = fct.get(n,0) + 1
        return fct
     
    
    mydict = defaultdict(int)
    for i in a:
        x = pf(i)
        for k,v in x.items():
            mydict[k] += v

    f = 1
    for v in mydict.values():
        if v % n:
            f = 0
            break
    print(yn(f))



    return

ttt = ni()
for _ in range(test(ttt)):
    solve()