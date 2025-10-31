# Problem: k-Factorization - https://codeforces.com/problemset/problem/797/A

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
    fact = []

    while n % 2 == 0:
        fact.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while  n%i == 0:
            fact.append(i)
            n //= i
    if n > 2:
        fact.append(n)
    if len(fact) < k:
        return print(-1)
    if len(fact) == k:
        return print(*fact)
    
    x = len(fact) - k
    num = 1
    for i in range(x+1):
        num *= fact[i]
    num = [num]
    num.extend(fact[x+1:])
    print(*num)
    
    



    return

ttt = 1
for _ in range(test(ttt)):
    solve()