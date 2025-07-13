# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

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
    cnt = [0] * 30  
    for i in a:
        for j in range(30):
            if i & (1 << j):
                cnt[j] += 1
    # print(cnt)
    x = 0
    for count in cnt:
        x = math.gcd(x, count)
    
    for k in range(1, n + 1):
        if x % k == 0:
            print(k,end=" ")
    
    print()


    return

ttt = ni()
for _ in range(test(ttt)):
    solve()

